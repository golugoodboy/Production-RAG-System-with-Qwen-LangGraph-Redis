from typing import List, TypedDict
from langchain_core.documents import Document

class GraphState(TypedDict):
    question : str
    answer : str
    docs : List[Document]
    history: list




    