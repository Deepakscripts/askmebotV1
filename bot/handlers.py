from aiogram import Router
from bot.core import router as core_router
from bot.rag import router as rag_router

# Combine routers into one parent router so we only attach once
main_router = Router()
main_router.include_router(core_router)
main_router.include_router(rag_router)