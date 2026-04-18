# 📘 NotebookLM Replica (Capstone Project)

## 🚀 Project Overview

This project is a simplified clone of NotebookLM built using Streamlit and Python.
It allows users to upload PDFs, chat with documents using AI (RAG), perform optional web search, and save important notes.

---

## 🎯 Features

### ✅ Day 1 – Prompt Engineering

* AI chat interface using local LLM (Ollama)
* Structured prompts for better responses

### ✅ Day 2 – Document Processing

* Upload PDF files
* Extract and split content using RecursiveCharacterTextSplitter

### ✅ Day 3 – RAG (Retrieval Augmented Generation)

* Store document chunks in ChromaDB
* Retrieve top relevant chunks
* Answer questions based on uploaded documents

### ✅ Day 4 – Agents & Tools

* Document search tool
* Web search using Tavily API
* Save notes tool

### ✅ Day 5 – LangGraph Workflow

* Intent classification
* Conditional routing
* Response generation pipeline

---

## 🛠️ Tech Stack

* Frontend: Streamlit
* LLM: Ollama (llama3.2:3b)
* Framework: LangChain
* Vector DB: ChromaDB
* Embeddings: nomic-embed-text
* Web Search: Tavily API
* Orchestration: LangGraph

---

## 📁 Project Structure

```
notebook-lm/
├── app.py
├── components/
├── core/
├── storage/
│   ├── uploads/
│   ├── chroma_db/
│   └── notes/
```

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Install Ollama

Download: https://ollama.com

```
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

### 3. Run the app

```
streamlit run app.py
```

---

## 🔑 Environment Variables

Create `.env` file:

```
TAVILY_API_KEY=your_api_key_here
OLLAMA_BASE_URL=http://localhost:11434
```

---

## 📸 Screenshots

(Add your screenshots here)

---

## 🎥 Demo

(Add demo video link here)

---

## 💡 Learning Outcome

* Built an end-to-end AI application
* Learned RAG, Agents, and LangGraph
* Integrated local LLM with real-world use case

---

## 🙌 Acknowledgement

Nunnari Academy – Generative AI Bootcamp
