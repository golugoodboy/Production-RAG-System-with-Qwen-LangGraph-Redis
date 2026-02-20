import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses = True)

def get_cached_answer(query: str):
    return r.get(f"cache:{query}")


def set_cached_answer(query: str, answer: dict):
    r.set(f"cache:{query}", json.dumps(answer))

def get_history(session_id: str):
    data = r.get(f"session:{session_id}")
    if data:
        return json.loads(data)
    return []


def save_history(session_id: str, history: list):
    r.set(f"session:{session_id}", json.dumps(history))