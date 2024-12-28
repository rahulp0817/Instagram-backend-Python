from fastapi import APIRouter, HTTPException
from app.database import db
from app.models.post import Post

router = APIRouter()

@router.post("/")
async def create_post(post: Post):
    await db.posts.insert_one(post.dict())
    return {"message": "Post created successfully"}

@router.get("/{post_id}")
async def get_post(post_id: str):
    post = await db.posts.find_one({"_id": post_id})
    if post:
        return post
    raise HTTPException(status_code=404, detail="Post not found")