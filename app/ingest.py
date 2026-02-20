import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import faiss
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings

class localEmbeddings(Embeddings):
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, texts):
        return self.model.encode(texts, normalize_embeddings=True).tolist()

    def embed_query(self, text):
        return self.model.encode([text], normalize_embeddings=True).tolist()[0]


if __name__ == "__main__":
    data_path = "data/"
    docs = []

    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            try:
                loader = PyPDFLoader(os.path.join(data_path, file))
                docs.extend(loader.load())
            except Exception as e:
                print(f"Error loading {file}: {e}")

    print(f"Loaded {len(docs)} documents.")


    #chunking documents

    splitter = RecursiveCharacterTextSplitter(chunk_size = 800, chunk_overlap = 150)
    chunks = splitter.split_documents(docs)

    print(f"Chunked {len(chunks)} documents.")

    #embeddings documents

    embeddings = localEmbeddings()

    #vector store
    vector_db = FAISS.from_documents(chunks, embeddings)

    vector_db.save_local("vector_store")

    print("FAISS index saved.")





