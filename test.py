from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"message": "Published content", "limit": limit}
    else:
        return {"message": "Unpublished content", "limit": limit}
    

@app.get("blog/{id}/comments")
def comments(id, limit=10):
    return limit

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(request: Blog):
    return {"message": "Blog created successfully"}



# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)