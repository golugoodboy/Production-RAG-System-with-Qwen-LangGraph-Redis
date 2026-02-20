"""
Loads FAISS vector store and exposes retriever
Production-ready version
"""

from langchain_community.vectorstores import FAISS
from app.ingest import localEmbeddings

vector_path = "vector_store"
top_k = 6

embedding = localEmbeddings()

def load_vector_store():
    return FAISS.load_local(vector_path, embedding, allow_dangerous_deserialization = True)


vector_db = load_vector_store()

retriever = vector_db.as_retriever(search_type="similarity", k = top_k)













