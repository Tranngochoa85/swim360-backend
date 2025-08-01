from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class BookingStatus(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(SQLAlchemyEnum(BookingStatus), default=BookingStatus.PENDING)
    final_fee = Column(Float, nullable=True)

    # Foreign Keys
    learner_id = Column(Integer, ForeignKey("users.id"))
    coach_id = Column(Integer, ForeignKey("users.id"))
    pool_id = Column(Integer, ForeignKey("pools.id"))

    # Relationships
    learner = relationship("User", foreign_keys=[learner_id])
    coach = relationship("User", foreign_keys=[coach_id])
    pool = relationship("Pool", back_populates="bookings")

    # Bổ sung mối quan hệ còn thiếu
    transactions = relationship("Transaction", back_populates="booking")