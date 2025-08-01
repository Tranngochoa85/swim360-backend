from pydantic import BaseModel
from datetime import datetime
from typing import Union
from app.models.booking import BookingStatus

# --- Schemas đơn giản để lồng vào ---
class UserSimple(BaseModel):
    id: int
    full_name: Union[str, None] = None
    email: str
    class Config: from_attributes = True

class PoolSimple(BaseModel):
    id: int
    name: str
    class Config: from_attributes = True

# --- Schema chính ---

# Schema cho dữ liệu đầu vào khi Learner tạo một booking
class BookingCreate(BaseModel):
    pool_id: int
    coach_id: int
    # Các thông tin khác như thời gian, trình độ... sẽ được thêm sau

# Schema đầy đủ khi trả về dữ liệu Booking
class Booking(BaseModel):
    id: int
    status: BookingStatus
    final_fee: Union[float, None] = None
    created_at: datetime
    learner: UserSimple
    coach: UserSimple
    pool: PoolSimple
    class Config: from_attributes = True