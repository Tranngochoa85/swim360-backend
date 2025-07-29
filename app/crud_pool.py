from sqlalchemy.orm import Session
from app import models, schemas

def register_pool(db: Session, pool_data: schemas.PoolRegister, owner_id: int):
    """
    Tạo một bản ghi hồ bơi mới với trạng thái chờ duyệt.
    """
    full_address = f"{pool_data.address}, {pool_data.district}, {pool_data.city}"

    db_pool = models.Pool(
        name=pool_data.name,
        address=full_address,
        owner_id=owner_id,
        # Các trường khác sẽ có giá trị mặc định (như status='pending_approval')
    )
    db.add(db_pool)
    db.commit()
    db.refresh(db_pool)
    return db_pool