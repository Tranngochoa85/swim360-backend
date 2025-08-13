from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, crud_coach
from app.security import get_db, get_current_active_coach

router = APIRouter()

@router.put("/me/profile", response_model=schemas.CoachProfile, summary="Create or update the current coach's profile")
def update_my_profile(
    profile_data: schemas.CoachProfileCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_coach)
):
    """
    Endpoint cho HLV tự tạo hoặc cập nhật hồ sơ của chính mình.
    """
    profile = crud_coach.create_or_update_coach_profile(db=db, profile_data=profile_data, user_id=current_user.id)
    return profile