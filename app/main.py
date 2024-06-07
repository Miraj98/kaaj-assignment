from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import Database

app = FastAPI()
db = Database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/search")
async def search(name: str | None = None, city: str | None = None, state: str | None = None, cursor: int | None = 0, page_size: int = 50):
    res = db.search_query(name, city, state, cursor, page_size)
    if type(res) is not list:
        return { 'data': [], 'cursor': None, 'has_more': False }
    if len(res) < page_size:
        return { 'data': res, 'cursor': None, 'has_more': False }
    return { 'data': res, 'cursor': res[-1]['id'], 'has_more': True }

