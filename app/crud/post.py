from sqlalchemy.orm import Session
from app.models import post as post_models
from app.schemas import post as post_schemas

def create_post(db: Session, post: post_schemas.PostCreate, user_id: int):
    db_post = post_models.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db: Session, post_id: int):
    return db.query(post_models.Post).filter(post_models.Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(post_models.Post).offset(skip).limit(limit).all()

def update_post(db: Session, post_id: int, post_data: post_schemas.PostUpdate):
    db_post = db.query(post_models.Post).filter(post_models.Post.id == post_id).first()
    if db_post:
        for key, value in post_data.dict(exclude_unset=True).items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(post_models.Post).filter(post_models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post