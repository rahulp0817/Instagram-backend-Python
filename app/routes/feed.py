from fastapi import APIRouter, HTTPException
from app.database import db

router = APIRouter()

@router.get('/')
async def get_feed(user_id: str, skip: int = 0, limit: int = 10):
    user = await db.users.find_one({"_id": user_id})
    if not user:
        return []
    
    follow_id = user.get('following', [])
    posts = await db.posts.find({"publisher_id": {"$in": follow_id}}).sort("datetime_posted", -1).skip(skip).limit(limit).to_list(length=limit)

    return posts