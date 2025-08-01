from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, models, crud_admin
from app.security import get_db, get_current_active_admin

router = APIRouter()

@router.get("/pools/pending", response_model=List[schemas.Pool], summary="Get pending pools")
def get_pending_pools_for_admin(
    db: Session = Depends(get_db),
    admin_user: models.User = Depends(get_current_active_admin)
):
    pools = crud_admin.get_pending_pools(db=db)
    return pools

@router.post("/pools/{pool_id}/approve", response_model=schemas.Pool, summary="Approve a pool")
def approve_pool_endpoint(
    pool_id: int,
    db: Session = Depends(get_db),
    admin_user: models.User = Depends(get_current_active_admin)
):
    pool = crud_admin.get_pool_by_id(db, pool_id=pool_id)
    if not pool:
        raise HTTPException(status_code=404, detail="Pool not found")
    if pool.status != models.PoolStatus.PENDING_APPROVAL:
        raise HTTPException(status_code=400, detail="Pool is not in pending state")

    return crud_admin.approve_pool(db=db, pool=pool)

@router.post("/pools/{pool_id}/reject", response_model=schemas.Pool, summary="Reject a pool")
def reject_pool_endpoint(
    pool_id: int,
    db: Session = Depends(get_db),
    admin_user: models.User = Depends(get_current_active_admin)
):
    pool = crud_admin.get_pool_by_id(db, pool_id=pool_id)
    if not pool:
        raise HTTPException(status_code=404, detail="Pool not found")
    if pool.status != models.PoolStatus.PENDING_APPROVAL:
        raise HTTPException(status_code=400, detail="Pool is not in pending state")

    return crud_admin.reject_pool(db=db, pool=pool)
@router.get("/users/", response_model=List[schemas.User], summary="Get a list of all users")
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    admin_user: models.User = Depends(get_current_active_admin)
):
    """
    Lấy danh sách người dùng.
    Chỉ có Admin mới có thể truy cập.
    """
    users = crud_admin.get_users(db, skip=skip, limit=limit)
    return users
@router.patch("/users/{user_id}/role", response_model=schemas.User, summary="Update a user's role")
def update_a_user_role(
    user_id: int,
    role_update: schemas.UserRoleUpdate,
    db: Session = Depends(get_db),
    admin_user: models.User = Depends(get_current_active_admin)
):
    """
    Cập nhật vai trò của một người dùng cụ thể.
    Chỉ có Admin mới có thể truy cập.
    """
    user_to_update = crud_admin.get_user_by_id(db, user_id=user_id)
    if not user_to_update:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = crud_admin.update_user_role(db=db, user=user_to_update, new_role=role_update.role)
    return updated_user
@router.get("/bookings/", response_model=List[schemas.Booking], summary="Get a list of all bookings")
def read_bookings(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    admin_user: models.User = Depends(get_current_active_admin)
):
    """
    Lấy danh sách tất cả các khóa học trong hệ thống.
    Chỉ có Admin mới có thể truy cập.
    """
    bookings = crud_admin.get_bookings(db, skip=skip, limit=limit)
    return bookings
@router.get("/transactions/", response_model=List[schemas.Transaction], summary="Get a list of all transactions")
def read_transactions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    admin_user: models.User = Depends(get_current_active_admin)
):
    """
    Lấy danh sách tất cả các giao dịch trong hệ thống.
    Chỉ có Admin mới có thể truy cập.
    """
    transactions = crud_admin.get_transactions(db, skip=skip, limit=limit)
    return transactions