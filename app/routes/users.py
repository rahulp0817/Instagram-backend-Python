from fastapi import APIRouter, HTTPException
from app.database import db
from bson import ObjectId

router = APIRouter()
def serialize_dict(d):
    return {str(k): str(v) if isinstance(v, ObjectId) else v for k, v in d.items()}

def serialize_list(entity):
    return [serialize_dict(a) for a in entity]

@router.get('/{username}')
async def get_user(username: str):
    user = await db.users.find_one({"username": username})
    if user:
      return serialize_dict(user)
    raise HTTPException(status_code=404, detail="User not found")