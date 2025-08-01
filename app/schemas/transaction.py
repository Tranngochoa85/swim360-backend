from pydantic import BaseModel
from datetime import datetime
from typing import Union
from app.models.transaction import TransactionStatus

class BookingSimple(BaseModel):
    id: int
    class Config: from_attributes = True

class Transaction(BaseModel):
    id: int
    amount: float
    platform_fee: float
    status: TransactionStatus
    created_at: datetime
    booking: BookingSimple

    class Config:
        from_attributes = True