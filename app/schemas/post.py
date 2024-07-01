from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: str = None
    content: str = None

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
