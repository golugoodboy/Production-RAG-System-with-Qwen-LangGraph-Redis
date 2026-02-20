from fastapi import FastAPI
from app.pipeline import ask_rag
from pydantic import BaseModel
import time
import logging


logging.basicConfig(
    filename = "logs/app.log",
    level = logging.INFO,
    format = "%(asctime)s - %(message)s"    
)

app = FastAPI(title = "Production RAG System")


class QueryRequest(BaseModel):
    question : str
    session_id: str

@app.post("/ask")
def ask_endpoint(req : QueryRequest):
    start = time.time()

    result = ask_rag(req.question, req.session_id)

    latency = round(time.time() - start,2)

    logging.info(f"Q: {req.question}")
    logging.info(f"Latency: {latency}s")

    return {
        "answer": result["answer"],
        "sources": result["sources"],
        "latency": latency
    }








