from langgraph.graph import StateGraph, END
from typing_extensions import TypedDict
from typing import List
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

#State Structure
class StudyState(TypedDict):
    pdf_path: str
    docs: list
    vectorstore: object
    summary: str
    flashcards: List[str]
    topic: str


# Loading our pdf
def load_pdf_node(state: StudyState):
    if "pdf_path" not in state or not state["pdf_path"]:
        state["pdf_path"] = "data/software_notes.pdf"

    loader = PyPDFLoader(state["pdf_path"])
    state["docs"] = loader.load()
    return state



#Embedding & Vector Store
def embed_node(state: StudyState):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(state["docs"])

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    state["vectorstore"] = FAISS.from_documents(chunks, embeddings)
    return state


# Summary
def summary_node(state: StudyState):
    docs = state["vectorstore"].similarity_search("overview", k=10)
    combined = "\n\n".join(d.page_content for d in docs)

    state["summary"] = llm.invoke(
        f"Summarize clearly for easy studying:\n\n{combined}"
    ).content
    return state


# Topic wise (custom)
def topic_query_node(state: StudyState):
    topic = state.get("topic", "overall concepts") 

    docs = state["vectorstore"].similarity_search(topic, k=10)
    text = "\n\n".join(d.page_content for d in docs)

    state["summary"] = llm.invoke(
        f"Summarize only the topic '{topic}' clearly for revision:\n\n{text}"
    ).content

    state["flashcards"] = llm.invoke(
        f"Generate 10 flashcards (Q/A only) for topic: {topic}\n\n{text}"
    ).content.split("\n\n")

    return state



# Flashcards
def flashcard_node(state: StudyState):
    docs = state["vectorstore"].similarity_search("overview", k=10)
    combined = "\n\n".join(d.page_content for d in docs)

    flash = llm.invoke(
        "Generate 10 flashcards in Q/A format only:\n" + combined
    ).content.split("\n\n")

    state["flashcards"] = flash
    return state


#Building our nodes and graphs
graph = StateGraph(StudyState)

graph.add_node("LOAD_PDF", load_pdf_node)
graph.add_node("EMBED", embed_node)
graph.add_node("SUMMARY", summary_node)
graph.add_node("FLASHCARDS", flashcard_node)
graph.add_node("TOPIC_QUERY", topic_query_node)

graph.set_entry_point("LOAD_PDF")
graph.add_edge("LOAD_PDF", "EMBED")
graph.add_edge("EMBED", "SUMMARY")
graph.add_edge("SUMMARY", "FLASHCARDS")
graph.add_edge("FLASHCARDS", "TOPIC_QUERY")
graph.add_edge("FLASHCARDS", END)

app = graph.compile()

if __name__ == "__main__":
    result = app.invoke({"pdf_path": "data/software_notes.pdf"})
    print(result)
