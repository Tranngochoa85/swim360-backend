from sqlalchemy.orm import Session
from . import models, schemas, security

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        full_name=user.full_name,
        role=user.role,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    """
    Lấy danh sách tất cả các giao dịch.
    """
    return db.query(models.Transaction).offset(skip).limit(limit).all()