from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import SessionLocal, engine
from app.crud import post as post_crud
from app.schemas import post as post_schemas
from app.models import post as post_models

post_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/posts/", response_model=post_schemas.Post)
def create_post(post: post_schemas.PostCreate, user_id: int, db: Session = Depends(get_db)):
    return post_crud.create_post(db=db, post=post, user_id=user_id)

@router.get("/posts/", response_model=List[post_schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = post_crud.get_posts(db, skip=skip, limit=limit)
    return posts

@router.get("/posts/{post_id}", response_model=post_schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = post_crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.put("/posts/{post_id}", response_model=post_schemas.Post)
def update_post(post_id: int, user: post_schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = post_crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.update_post(db=db, post_id=post_id, post=post)

@router.delete("/posts/{post_id}", response_model=post_schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = post_crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    post_crud.delete_post(db=db, post_id=post_id)
    return db_post