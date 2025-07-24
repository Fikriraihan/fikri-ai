# 🤖 Fikri AI — Personalized Assistant Backend

This is the backend for **Fikri Raihan's personal AI assistant**, built using FastAPI, LangChain, and OpenAI to answer questions about Fikri's professional experience, projects, and profile.

---

## ✨ Features

- 🔎 **Retrieval-Augmented Generation (RAG)** using LangChain & Chroma
- 🧠 **Memory-aware chat** with conversation context
- 🗂️ Smart document indexing from Markdown, PDF, and TXT
- 🌐 API-ready backend for frontend integration (e.g. Netlify)
- 🚀 Production-ready via Docker

---

## 📁 Project Structure

bash
.
├── app.py # FastAPI app (main entry point)
├── Dockerfile # For production deployment
├── requirements.txt # Python dependencies
├── pyproject.toml # Optional project metadata (for uv)
├── .gitignore
├── fikri/ # Knowledge base folder (markdown, PDFs, etc)
│ ├── interview/
│ ├── Planet Surf/
│ ├── Reycom Document Solusi/
│ └── me/
