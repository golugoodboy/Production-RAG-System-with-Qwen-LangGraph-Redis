from app.hybrid_retriever import hybridsearch
from app.reranker import rerank
from app.prompt import build_prompt
from app.llm import generate_answer
from app.graph_state import GraphState

def retrieve_node(state):
    query = state["question"]

    docs = hybridsearch(query)
    docs = rerank(query,docs,top_k = 3)

    return {"docs" : docs}  

def generate_node(state):
    query = state["question"]
    docs = state["docs"]
    history = state.get("history", [])

    context = build_prompt(query, docs)

    history_text = ""
    for turn in history[-3:]:   # keep last 3 turns only
        history_text += f"User: {turn['user']}\n"
        history_text += f"Assistant: {turn['assistant']}\n"

    final_prompt = f"""
Conversation history:
{history_text}

{context}
"""

    answer = generate_answer(final_prompt)

    return {"answer": answer}

