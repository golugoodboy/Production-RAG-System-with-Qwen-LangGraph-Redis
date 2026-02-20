from app.pipeline import ask_rag

while True:
    q = input("Ask: ")
    res = ask_rag(q)
    print("\nANSWER:\n", res["answer"])