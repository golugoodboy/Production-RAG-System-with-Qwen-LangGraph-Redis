from rank_bm25 import BM25Okapi
from app.retriever import vector_db

docs = vector_db.docstore._dict.values()
texts = [d.page_content for d in docs]

tokenized =  [t.split() for t in texts]

bm25 = BM25Okapi(tokenized)

documents = list(docs)

def bm25search(query, k = 5):
    tokens = query.split()
    scores = bm25.get_scores(tokens)

    ranked = sorted(
        zip(documents,scores),
        key = lambda x : x[1],
        reverse = True
    )

    return [doc for doc,score in ranked[:k]]



