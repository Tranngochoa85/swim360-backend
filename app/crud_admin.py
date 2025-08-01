from sqlalchemy.orm import Session
from app import models

def get_pending_pools(db: Session, skip: int = 0, limit: int = 100):
    """
    Lấy danh sách các hồ bơi đang ở trạng thái chờ duyệt.
    """
    return db.query(models.Pool).filter(models.Pool.status == models.PoolStatus.PENDING_APPROVAL).offset(skip).limit(limit).all()

def get_pool_by_id(db: Session, pool_id: int):
    """
    Lấy một hồ bơi theo ID.
    """
    return db.query(models.Pool).filter(models.Pool.id == pool_id).first()

def approve_pool(db: Session, pool: models.Pool):
    """
    Cập nhật trạng thái hồ bơi thành 'approved'.
    """
    pool.status = models.PoolStatus.APPROVED
    db.commit()
    db.refresh(pool)
    return pool

def reject_pool(db: Session, pool: models.Pool):
    """
    Cập nhật trạng thái hồ bơi thành 'rejected'.
    """
    pool.status = models.PoolStatus.REJECTED
    db.commit()
    db.refresh(pool)
    return pool
def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Lấy danh sách tất cả người dùng.
    """
    return db.query(models.User).offset(skip).limit(limit).all()
def get_user_by_id(db: Session, user_id: int):
    """
    Lấy một người dùng theo ID.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user_role(db: Session, user: models.User, new_role: models.UserRole):
    """
    Cập nhật vai trò cho một người dùng.
    """
    user.role = new_role
    db.commit()
    db.refresh(user)
    return user
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    """
    Lấy danh sách tất cả các khóa học.
    """
    return db.query(models.Booking).offset(skip).limit(limit).all()
def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    """
    Lấy danh sách tất cả các giao dịch.
    """
    return db.query(models.Transaction).offset(skip).limit(limit).all()