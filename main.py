from fastapi import FastAPI
from dotenv import load_dotenv

from chatgpt.routes import router as chat_router

import openai
import os

# pip install poetry
# poetry shell
# import 추가될 때마다 poetry update 실행 해주어야 함
# uvicorn main:app --reload  으로 프로젝트 실행
# http://localhost:8000/docs 로 접속

app = FastAPI()

app.include_router(chat_router)
