from fastapi import FastAPI
from dotenv import load_dotenv

from chatgpt.routes import router as chat_router

import openai
import os

load_dotenv()
app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")



app.include_router(chat_router)
