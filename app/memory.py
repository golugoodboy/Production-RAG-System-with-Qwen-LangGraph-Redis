"""
Simple in-memory conversation store.
Session-based memory.
"""

memory_store = {}

def get_history(session_id: str):
    return memory_store.get(session_id, [])

def add_to_history(session_id: str, user_msg: str, ai_msg: str):
    history = memory_store.get(session_id, [])

    history.append({
        "user": user_msg,
        "assistant": ai_msg
    })

    memory_store[session_id] = history

