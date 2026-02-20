import time
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2-7B-Instruct",
    task="text-generation",
    max_new_tokens = 300,
    do_sample = False,
    temperature=0.1,
    repetition_penalty=1.1,
    huggingfacehub_api_token = ''
)


model = ChatHuggingFace(llm = llm)



def generate_answer(prompt : str) -> str:
    """
    Calls Qwen LLM with retry logic.
    Used by RAG pipeline.
    """

    retries = 3
    for attempt in range(retries):
        try:
            response = model.invoke(prompt)
            return response.content
        except Exception as e:
            print(f"[LLM ERROR] Attempt {attempt+1}: {e}")
            time.sleep(2)
    return "Error: Failed to generate answer after multiple retries."



