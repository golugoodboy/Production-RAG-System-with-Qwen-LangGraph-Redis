from langgraph.graph import StateGraph, START, END
from app.graph_state import GraphState
from app.graph_nodes import retrieve_node, generate_node
from app.rewrite_node import rewrite_node

graph = StateGraph(GraphState)

graph.add_node("retriever", retrieve_node)
graph.add_node("generate", generate_node)
graph.add_node("rewrite", rewrite_node)

graph.add_edge(START, "rewrite")
graph.add_edge("rewrite", "retriever")
graph.add_edge("retriever", "generate")
graph.add_edge("generate", END)

workflow = graph.compile()

