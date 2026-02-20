max_prompt = 2500

def build_prompt(query, docs):
    context = "\n\n".join([d.page_content for d in docs])

    content = context[:max_prompt]
    return f"""
You are a helpful AI assistant.
Answer ONLY using the provided context.
If answer not in context, say "Not found in documents."

Context:
{content}

Question:
{query}
"""

