from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
  id: int
  caption: str
  image_url: str
  posted_at: datetime = datetime.now()
  publisher_id: str
  category: str