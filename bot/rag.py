import os
import re
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.llm import llm, set_vectorstore, get_vectorstore, search_tool

router = Router()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Helpers ---
def unwrap_tavily_result(raw):
    """Handle Tavily return types (dict, list, FieldInfo)."""
    if isinstance(raw, dict) and "results" in raw:
        return raw["results"]
    if hasattr(raw, "results"):
        try:
            return getattr(raw, "results")
        except Exception:
            return str(raw)
    return raw

def normalize_search_results(results):
    if isinstance(results, str):
        return results
    if isinstance(results, list):
        return "\n".join(res.get("content", str(res)) for res in results)
    return str(results)

def is_realtime_query(query: str) -> bool:
    keywords = [
        r"\bweather\b", r"\btemperature\b", r"\btoday\b", r"\bnow\b",
        r"\bcurrent\b", r"\bnews\b", r"\bstock\b", r"\bprice\b",
        r"\bscore\b", r"\bupdate\b", r"\blatest\b", r"\bflight\b"
    ]
    return any(re.search(kw, query.lower()) for kw in keywords)

# --- PDF Upload ---
@router.message(Command("upload"))
async def upload_prompt(message: Message):
    await message.answer("Please send me the PDF file (as a document).")

@router.message(lambda m: m.document is not None)
async def handle_pdf(message: Message, bot):
    file = message.document
    path = f"downloads/{file.file_name}"
    os.makedirs("downloads", exist_ok=True)

    file_info = await bot.get_file(file.file_id)
    await bot.download_file(file_info.file_path, path)

    loader = PyPDFLoader(path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    set_vectorstore(vectorstore)

    await message.answer(f"PDF '{file.file_name}' processed! Ask me questions about it.")

# --- Main Chat ---
@router.message()
async def chat_handler(message: Message):
    query = message.text
    context = ""

    # Check PDF RAG
    store = get_vectorstore()
    if store:
        retriever = store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        docs = retriever.get_relevant_documents(query)
        context = "\n".join(doc.page_content for doc in docs)

    # Fallback to web search if real-time info or no context
    if not context.strip() or is_realtime_query(query):
        raw = search_tool.run(query)
        context = normalize_search_results(unwrap_tavily_result(raw))

    # Final LLM Response
    prompt = f"Context:\n{context}\n\nUser Question: {query}\nAnswer concisely (50 words max)."
    result = llm.invoke(prompt)
    response = result.content if hasattr(result, "content") else str(result)

    await message.answer(response)
