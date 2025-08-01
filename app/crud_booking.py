from sqlalchemy.orm import Session
from app import models, schemas

def create_booking(db: Session, booking_data: schemas.BookingCreate, learner_id: int):
    """
    Tạo một booking mới.
    """
    db_booking = models.Booking(
        pool_id=booking_data.pool_id,
        coach_id=booking_data.coach_id,
        learner_id=learner_id
        # status mặc định là 'pending'
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking