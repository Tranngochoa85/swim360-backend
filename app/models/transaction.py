from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class TransactionStatus(enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    amount = Column(Float, nullable=False)
    platform_fee = Column(Float, nullable=False)
    status = Column(SQLAlchemyEnum(TransactionStatus), default=TransactionStatus.PENDING)
    payment_gateway_ref_id = Column(String, nullable=True, index=True)

    booking_id = Column(Integer, ForeignKey("bookings.id"))
    booking = relationship("Booking", back_populates="transactions")