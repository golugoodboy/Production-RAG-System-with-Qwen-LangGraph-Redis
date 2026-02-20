from app.graph import workflow
from app.memory import get_history, add_to_history
from app.redis_client import (
    get_cached_answer,
    set_cached_answer,
    get_history,
    save_history
)
import json

def ask_rag(query: str, session_id: str):

    # -------------------------
    # Check Cache
    # -------------------------
    cached = get_cached_answer(query)
    if cached:
        return json.loads(cached)

    # -------------------------
    # Get Conversation History
    # -------------------------
    history = get_history(session_id)

    # -------------------------
    # Run LangGraph
    # -------------------------
    result = rag_graph.invoke({
        "query": query,
        "docs": [],
        "answer": "",
        "history": history
    })

    sources = list(set(
        d.metadata.get("source", "unknown")
        for d in result.get("docs", [])
    ))

    response = {
        "answer": result.get("answer", ""),
        "sources": sources
    }

    # -------------------------
    # Save to Memory
    # -------------------------
    history.append({
        "user": query,
        "assistant": response["answer"]
    })

    save_history(session_id, history)

    # -------------------------
    # Save to Cache
    # -------------------------
    set_cached_answer(query, response)

    return response
















