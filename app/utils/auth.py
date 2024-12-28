from passlib.hash import bcrypt
from jose import jwt   
from app.config import JWT_SECRET

def hash_password(password: str):
    return bcrypt.hash(password)

def verify_password(password: str, hashed: str):
    return bcrypt.verify(password, hashed)

def create_access_token(data: dict):
    return jwt.encode(data, JWT_SECRET, algorithm="HS256")