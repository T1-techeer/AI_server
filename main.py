from fastapi import FastAPI
from dotenv import load_dotenv

from chatgpt.routes import router as chat_router

import openai
import os

app = FastAPI()





app.include_router(chat_router)
