import os
import glob
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['https://fikri-portofolio.netlify.app', 'http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Ganti jadi domainmu kalau perlu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str
    history: list = []


# =================== Load ENV and Define Model ===================

load_dotenv()
MODEL = "gpt-4o-mini"
db_name = "vector_db"

# =================== Load & Split Documents ===================

folders = glob.glob("fikri/*")
text_loader_kwargs = {'encoding': 'utf-8'}

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "title"),
        ("##", "section"),
        ("###", "subsection")
    ]
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1800,
    chunk_overlap=250,
    separators=["\n\n", "\n", ".", " ", ""]
)

def add_metadata(doc, doc_type):
    doc.metadata["doc_type"] = doc_type
    doc.metadata["source"] = doc.metadata.get("source", os.path.basename(doc.metadata.get("source", doc_type)))
    return doc


documents = []
for folder in folders:
    company_name = os.path.basename(folder)  # sekarang ini nama perusahaan: Planet Surf, RDS, etc

    md_loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
    md_docs_raw = md_loader.load()
    md_docs = []

    for doc in md_docs_raw:
        filename = os.path.basename(doc.metadata.get("source", ""))

        # cari periode dari markdown header
        lines = doc.page_content.splitlines()
        period = ""
        for line in lines:
            if line.lower().startswith("- **period:**"):
                period = line.split("**Period:**")[-1].strip()
                break

        # markdown heading split
        splits = markdown_splitter.split_text(doc.page_content)

        for split in splits:
            section_title = split.metadata.get("section", "")
            is_project = section_title.strip().startswith("📁 Project:")

            metadata = {
                **doc.metadata,
                **split.metadata,
                "company": company_name,       # <== updated dari folder
                "filename": filename,
                "period": period,
                "doc_type": "work-experience" if "Project" in section_title else "general"
            }

            metadata["title"] = section_title.replace("📁 Project: ", "").strip() if is_project else None


            md_docs.append(Document(
                page_content=split.page_content,
                metadata=metadata
            ))

    # load pdf & txt (opsional metadata bisa ditambahkan juga)
    pdf_loader = DirectoryLoader(folder, glob="**/*.pdf", loader_cls=PyPDFLoader)
    pdf_docs = text_splitter.split_documents(pdf_loader.load())

    txt_loader = DirectoryLoader(folder, glob="**/*.txt", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
    txt_docs = text_splitter.split_documents(txt_loader.load())

    all_docs = md_docs + pdf_docs + txt_docs
    documents.extend(all_docs)

# =================== Vector Store ===================

embeddings = OpenAIEmbeddings()

# Clean previous vectorstore
rebuild = os.getenv("REBUILD_VECTOR", "false").lower() == "true"

if os.path.exists(db_name) and not rebuild:
    vectorstore = Chroma(persist_directory=db_name, embedding_function=embeddings)
else:
    if os.path.exists(db_name):
        import shutil
        shutil.rmtree(db_name)
    vectorstore = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=db_name)


# =================== Prompt & Chain ===================

system_template = """You are acting as Fikri Raihan, a frontend developer with solid experience in React.js, TypeScript, Next.js, Zustand, Tailwind CSS, and modern frontend tooling. You speak as Fikri himself.

You are answering questions on Fikri's personal website or AI assistant, especially those related to his work history, projects, tech stack, achievements, or personal/professional background.

Fikri is currently work at Planet Surf. Previously, he worked at Reycom Document Solusi.

Fikri's Planet Surf projects include: Sales Panel, OTB Suite, Marketing Platform, and PU & Budgeting System. Reycom's projects include E2E & Supplier Apps, Cirrust Workflow, and Cirrust Document Management System.

You have access to a knowledge base that includes detailed project documentation, professional summaries, and past experiences from companies like Planet Surf and Reycom Document Solusi.

Your job is to:
- Respond to questions naturally and clearly from Fikri's perspective.
- Mention specific projects, companies, and roles when relevant.
- If a user asks about “other projects,” recall and summarize all known projects — don't limit your answer to the last one.
- If context includes multiple documents, synthesize them for a broader answer.
- If information is missing, say “I'm not sure about that” — never make things up.

Always list Fikri's work experience starting with the most recent. Be friendly, concise, and professional.

When asked about Fikri's projects, you should:
- Group them by company
- Mention the company name and period before listing projects
- Summarize each project clearly under that company
- Only include projects mentioned in the knowledge base
- Make sure you mention the right company for each project
- When referencing a project, make sure to associate it with the correct company based on the `company` metadata.
Do not mix up projects across companies.

To determine Fikri's current employer, always prioritize the most recent `period` from the metadata. 
If multiple companies are mentioned, choose the one with the latest `period`, such as "Aug 2024 – Present".

"""

human_template = """Context:
{context}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template)
])

retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
llm = ChatOpenAI(model_name=MODEL, temperature=0.7)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt},
)

# memory.clear()

def chat_api(request: ChatRequest):
    result = conversation_chain.invoke({
        "question": request.question,
        # kalau mau pakai history dari frontend
        # bisa mapping di sini
    })
    return {"answer": result["answer"]}

@app.post("/chat")
def chat(request: ChatRequest):
    if not request.history or len(request.history) == 0:
        memory.clear()  # hanya clear saat user tidak kirim history apa pun
    return chat_api(request)

@app.get("/")
def root():
    return {"message": "Fikri AI backend is running"}