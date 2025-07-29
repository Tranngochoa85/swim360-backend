from pydantic import BaseModel, Json
from typing import Union
from app.models.pool import PoolStatus

# Schema cho form đăng ký ban đầu (Giai đoạn 1)
class PoolRegister(BaseModel):
    name: str
    address: str
    district: str
    city: str
    phone: Union[str, None] = None
    email: Union[str, None] = None

# Schema đầy đủ của một hồ bơi (dùng sau này)
class Pool(BaseModel):
    id: int
    owner_id: int
    name: str
    address: str
    status: PoolStatus

    class Config:
        from_attributes = True