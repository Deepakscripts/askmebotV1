from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.llm import set_vectorstore

router = Router()

class Reference:
    def __init__(self):
        self.response = ""

reference = Reference()

def clear_past():
    reference.response = ""
    set_vectorstore(None)

@router.message(Command("clear"))
async def command_clear(message: Message):
    clear_past()
    await message.answer("Cleared conversation and any uploaded PDFs.")

@router.message(Command("start"))
async def command_start(message: Message):
    await message.answer(
        "Hello! I'm Deepak Agrawal, student of IIT, Mandi./n/n" 
        "This is *AskMeBotV1* - with general query + PDF (only text) + live info support.\n\n"
        "Ask any general question directly.\n"
        "Use /upload to give a PDF (only text) and ask questions.\n"
        "Live queries like 'What is weather in Delhi?' will auto-search.\n"
        "Use /clear to reset context and memory."
    )

@router.message(Command("help"))
async def command_help(message: Message):
    await message.answer(
        "Hi! I'm *AskMeBotV1*.\n\n"
        "Commands:\n"
        "/start — Welcome message\n"
        "/clear — Clear context + uploaded PDFs\n"
        "/upload — Upload a PDF (only text) to query\n"
        "/help — Show this menu again\n\n"
        "After uploading, you can ask things like:\n"
        "'Summarize page 2' or 'What does it say about AI?'"
    )
