# Production-RAG-System-with-Qwen-LangGraph-Redis
Production-ready RAG system built with Qwen, LangGraph, FAISS, and Redis. Supports hybrid search, reranking, streaming responses, and session-based memory via FastAPI. Demonstrates scalable AI backend architecture for document Q&amp;A and enterprise assistants.

# 🧠 Production RAG System with Qwen + LangGraph + Redis

A production-ready Retrieval-Augmented Generation (RAG) system built using:

- Qwen LLM (HuggingFace endpoint)
- LangGraph agent workflow
- Hybrid search (FAISS + BM25)
- Reranking
- Streaming responses
- Redis caching + memory
- FastAPI backend

This project demonstrates how to build a real-world AI backend similar to enterprise document assistants.

---

## 🚀 Features

### 🔎 Retrieval
- FAISS vector search
- BM25 keyword search
- Hybrid retrieval
- Cross-encoder reranking

### 🧠 LLM
- Qwen2-7B-Instruct via HuggingFace
- Optimized prompts
- Streaming responses

### 🕸 LangGraph Agent
- Query rewriting node
- Retrieval node
- Generation node
- Extensible graph workflow

### 💾 Redis Backend
- Persistent conversation memory
- Response caching
- Multi-session support

### 🌐 API
- FastAPI server
- Streaming endpoint
- Session-based chat

---

## 🏗 Architecture
User
↓
FastAPI
↓
LangGraph Agent
├─ Query Rewrite
├─ Hybrid Retrieval
├─ Reranker
└─ LLM Generation
↓
Redis
├─ Cache
└─ Memory
