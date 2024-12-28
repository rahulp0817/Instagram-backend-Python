from fastapi import APIRouter, HTTPException
from app.database import db

router = APIRouter()

@router.get('/users')
async def search_users(query:str):
  users = await db.users.find({"username": {"$regex": query}}).to_list(length=10)
  return users

@router.get("/posts")
async def search_posts(hashtag: str):
  posts = await db.posts.find({"caption": {"$regex": f"{hashtag}"}}).to_list(length=10)
  return posts