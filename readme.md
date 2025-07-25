# 🤖 Fikri AI — Personalized Assistant Backend

This is the backend for **Fikri Raihan's personal AI assistant**, built using FastAPI, LangChain, and OpenAI to answer questions about Fikri Raihan’s career, projects, tech stack, and experience — just like a portfolio chatbot..

👉 Try the frontend here: [fikri-portofolio.netlify.app](https://fikri-portofolio.netlify.app)  
⚠️ Backend hosted on Railway (may take time to spin up on free tier)

---

## ✨ Features

- 🔎 **Retrieval-Augmented Generation (RAG)** using LangChain & Chroma
- 🧠 **Memory-aware chat** with conversation context
- 🗂️ Smart document indexing from Markdown, PDF, and TXT
- 🌐 API-ready backend for frontend integration (e.g. Netlify)
- 🚀 Production-ready via Docker

---

## 📁 Project Structure

```
.
├── app.py                  # FastAPI app (main entry point)
├── Dockerfile              # For production deployment
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata
├── .gitignore
├── fikri/                  # Knowledge base folder (markdown, PDFs, etc)
│   ├── interview/
│   ├── Planet Surf/
│   ├── Reycom Document Solusi/
│   └── me/
```

---

## 🏗️ Tech Stack

| Area               | Stack/Library                           |
| ------------------ | --------------------------------------- |
| **API Server**     | FastAPI, Uvicorn                        |
| **RAG Pipeline**   | LangChain, OpenAI (GPT-4o-mini), Chroma |
| **Embeddings**     | `text-embedding-3-small` (OpenAI)       |
| **Frontend**       | React, Vite, Zustand (in separate repo) |
| **Deployment**     | Railway (API), Netlify (frontend)       |
| **Document Types** | Markdown (`.md`), PDF, TXT              |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/fikriraihan/fikri-ai.git
cd fikri-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or, if using `uv`:

```bash
uv pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file with your OpenAI API key and other configs:

```
OPENAI_API_KEY=your-openai-key
REBUILD_VECTOR=false
```

### 4. Run the App

```bash
uvicorn app:app --reload
```

### 5. (Optional) Run with Docker

```bash
docker build -t fikri-ai .
docker run -p 8000:8000 fikri-ai
```

---

## 📝 Adding Knowledge

- Place new Markdown, PDF, or TXT files in the `fikri/` directory.
- The vector store will auto-rebuild if `REBUILD_VECTOR=true` is set.

---

## 🛠️ Development

- Main logic in `app.py`
- Uses LangChain for RAG and ChromaDB for vector storage
- Custom prompt templates ensure answers are always up-to-date and grouped by company/project

---

## 📄 Example API Usage

```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={"question": "What projects did Fikri work on at Planet Surf?"}
)
print(response.json())
```

---
