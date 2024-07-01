from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud import comment as comment_crud
from app.schemas import comment as comment_schemas
from app.models import comment as comment_models
from app.db import SessionLocal, engine

comment_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/comments/", response_model=comment_schemas.Comment)
def create_comment(comment: comment_schemas.CommentCreate, user_id: int, post_id: int, db: Session = Depends(get_db)):
    return comment_crud.create_comment(db=db, comment=comment, user_id=user_id, post_id=post_id)

@router.get("/comments/", response_model=List[comment_schemas.Comment])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comments = comment_crud.get_comments(db, skip=skip, limit=limit)
    return comments

@router.get("/comments/{comment_id}", response_model=comment_schemas.Comment)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = comment_crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.put("/comments/{comment_id}", response_model=comment_schemas.Comment)
def update_comment(comment_id: int, comment: comment_schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = comment_crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return crud.update_comment(db=db, comment_id=comment_id, comment=comment)

@router.delete("/comments/{comment_id}", response_model=comment_schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = comment_crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    crud.delete_comment(db=db, comment_id=comment_id)
    return db_comment