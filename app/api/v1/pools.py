from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, crud_pool
from app.security import get_current_user, get_db

router = APIRouter()

@router.post("/register", response_model=schemas.Pool, summary="Register a new pool")
def register_new_pool(
    pool_data: schemas.PoolRegister,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Endpoint cho Chủ hồ bơi gửi thông tin đăng ký ban đầu.
    Hồ bơi sẽ được tạo với trạng thái 'pending_approval'.
    """
    if current_user.role != models.UserRole.POOL_OWNER:
        raise HTTPException(
            status_code=403, 
            detail="Forbidden: Not enough privileges."
        )

    return crud_pool.register_pool(db=db, pool_data=pool_data, owner_id=current_user.id)