from pydantic import BaseModel, EmailStr
from typing import List

class User(BaseModel):
  username: str
  email: EmailStr
  password: str
  followers : List[str] = []
  following : List[str] = []