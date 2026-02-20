"""Simple query rewriting node"""

from app.llm import generate_answer

def rewrite_node(state):
    query = state["question"]

    prompt = f"""
Rewrite the user question into a clear search query for document retrieval.
Keep it concise and factual.

User question:
{query}

Rewritten search query:
"""
    rewritten = generate_answer(prompt).strip()
    if not rewritten:
        rewritten = query

    return {"question": rewritten}

