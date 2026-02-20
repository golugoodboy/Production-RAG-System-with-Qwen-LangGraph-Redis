from FlagEmbedding import FlagReranker

reranker = FlagReranker(
    "BAAI/bge-reranker-base",
    use_fp16 = True
)


def rerank(query, docs, top_k = 4):
    texts = [d.page_content for d in docs]

    scores = reranker.compute_score(
        [[query,text] for text in texts]
    )

    ranked = sorted(zip(docs,scores), key = lambda x : x[1], reverse = True)

    return [doc for doc, score in ranked[:top_k]]