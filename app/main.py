from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.db import Database
from app.crawlers import crawl_data

app = FastAPI()
db = Database()


@app.get("/api/search/{search_str}")
async def search(search_str):
    return db.search_query(search_str)

@app.get("/api/crawl")
async def crawl():
    await crawl_data("penn")
    await crawl_data("florida")
    return { 'success': True }
