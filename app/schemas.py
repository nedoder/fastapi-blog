from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: str = None
    email: str = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


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