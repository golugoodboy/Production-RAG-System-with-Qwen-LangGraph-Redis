from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

def generate_answer(query, retriever):
    docs = retriever.similarity_search(query, k = 4)
    context = "\n".join([doc.page_content for doc in docs])
    
    prompt = f"""
    Answer using context only.

    Context:
    {context}

    Question:
    {query}
    """
    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2-7B-Instruct",
        task="text-generation",
        max_new_tokens = 512,
        do_sample = False,
        temperature=0.1)
    
    model = ChatHuggingFace(llm = llm)
    response = model.invoke(prompt)
    return response.content 