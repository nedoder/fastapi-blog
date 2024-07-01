from sqlalchemy.orm import Session
from app.models import comment as comment_models
from app.schemas import comment as comment_schemas

def create_comment(db: Session, comment: comment_schemas.CommentCreate, user_id: int, post_id: int):
    db_comment = comment_models.Comment(**comment.dict(), owner_id=user_id, post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment(db: Session, comment_id: int):
    return db.query(comment_models.Comment).filter(comment_models.Comment.id == comment_id).first()

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(comment_models.Comment).offset(skip).limit(limit).all()

def update_comment(db: Session, comment_id: int, comment_data: comment_schemas.CommentUpdate):
    db_comment = db.query(comment_models.Comment).filter(comment_models.Comment.id == comment_id).first()
    if db_comment:
        for key, value in comment_data.dict(exclude_unset=True).items():
            setattr(db_comment, key, value)
        db.commit()
        db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(comment_models.Comment).filter(comment_models.Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment