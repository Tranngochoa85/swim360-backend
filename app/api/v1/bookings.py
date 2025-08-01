from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, crud_booking
from app.security import get_current_user, get_db

router = APIRouter()

@router.post("/", response_model=schemas.Booking, summary="Create a new booking request")
def create_new_booking(
    booking_data: schemas.BookingCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Endpoint cho Người học (Learner) tạo một yêu cầu học bơi mới.
    """
    if current_user.role != models.UserRole.LEARNER:
        raise HTTPException(status_code=403, detail="Only learners can create bookings.")

    return crud_booking.create_booking(db=db, booking_data=booking_data, learner_id=current_user.id)