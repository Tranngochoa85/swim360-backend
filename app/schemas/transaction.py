from pydantic import BaseModel
from datetime import datetime
from typing import Union
from app.models.transaction import TransactionStatus

# Schema rút gọn cho Booking để lồng vào Transaction
class BookingSimpleForTransaction(BaseModel):
    id: int
    class Config:
        from_attributes = True

# Schema đầy đủ cho một Transaction
class Transaction(BaseModel):
    id: int
    amount: float
    platform_fee: float
    status: TransactionStatus
    created_at: datetime
    booking: BookingSimpleForTransaction

    class Config:
        from_attributes = True