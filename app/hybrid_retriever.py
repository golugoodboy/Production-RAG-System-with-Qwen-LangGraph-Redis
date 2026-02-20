from app.retriever import retriever
from app.hybrid import bm25search

def hybridsearch(query, k = 6):
    vector_docs = retriever.invoke(query)

    bm25_docs = bm25search(query, k = 6)

    combined = {id(doc): doc for doc in vector_docs}
    for doc in bm25_docs:
        combined[id(doc)] = doc

    return list(combined.values())[:k]

    