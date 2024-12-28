from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
  id: int
  post_id: int
  user_id: int
  content: str
  commented_at: datetime = datetime.now()
  likes: int = 0
  dislikes: int = 0
  comment_text: str 