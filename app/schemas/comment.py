from pydantic import BaseModel

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    content: str = None

class Comment(CommentBase):
    id: int
    owner_id: int
    post_id: int

    class Config:
        orm_mode = True