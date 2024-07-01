from sqlalchemy.orm import Session
from app.models import user as user_models
from app.schemas import user as user_schemas
from app.utils import hash

def create_user(db: Session, user: user_schemas.UserCreate):
    hashed_password = hash(user.password)
    user.password = hashed_password
    db_user = user_models.User(username=user.username, email=user.email, hashed_password=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(user_models.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_data: user_schemas.UserUpdate):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if db_user:
        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
