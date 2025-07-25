import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    temperature=0.3,
    model="gpt-4.1-nano",  # Or gpt-4o depending on your plan
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Tavily Search (for live internet queries)
search_tool = TavilySearch(
    max_results=3,
    search_depth="advanced"
)


# Shared Vectorstore (for PDFs)
_VECTORSTORE = None

def set_vectorstore(store):
    global _VECTORSTORE
    _VECTORSTORE = store

def get_vectorstore():
    return _VECTORSTORE
