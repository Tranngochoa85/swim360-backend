from sqlalchemy.orm import Session
from app import models, schemas

def create_or_update_coach_profile(db: Session, profile_data: schemas.CoachProfileCreate, user_id: int):
    """
    Tạo hoặc cập nhật hồ sơ cho một HLV.
    """
    # Tìm hồ sơ đã có
    db_profile = db.query(models.CoachProfile).filter(models.CoachProfile.user_id == user_id).first()

    if db_profile:
        # Nếu có, cập nhật
        update_data = profile_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_profile, key, value)
    else:
        # Nếu không, tạo mới
        db_profile = models.CoachProfile(**profile_data.dict(), user_id=user_id)
        db.add(db_profile)

    db.commit()
    db.refresh(db_profile)
    return db_profile