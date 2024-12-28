from fastapi import APIRouter, HTTPException
from app.database import db
from app.utils.auth import hash_password, create_access_token, verify_password
from pydantic import BaseModel

router = APIRouter()

class UserAuth(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register_user(user: UserAuth):
    user_exists = await db.users.find_one({"email": user.email})

    if user_exists:
        raise HTTPException(status_code=400, detail="User already exists")
    
    #hashed_password = hash_password(user.password)

    user_datas = {
        "username": user.username,
        "email": user.email,
        "password": user.password
    }

    await db.users.insert_one(user_datas)

    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: UserAuth):
    user_data = await db.users.find_one({"email": user.email})
    if not user_data or not verify_password(user.password, user_data["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"email": user.email})
    return {"access_token": token, "token_type": "bearer"}