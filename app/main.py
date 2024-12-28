from fastapi import FastAPI
from app.routes import auth, users, posts, feed, search

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users_Details"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(feed.router, prefix="/feed", tags=["Feeds"])
app.include_router(search.router, prefix="/search", tags=["Search Users and Posts"])

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to instagram backend app!"}