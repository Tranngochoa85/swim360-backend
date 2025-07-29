from pydantic import BaseModel
from datetime import datetime
from typing import Union, List
from ..models.user import UserRole, UserGoal # Import Enum từ model
from .pool import Pool # Import schema Pool để lồng vào User

# Schema cơ bản
class UserBase(BaseModel):
    email: str
    full_name: Union[str, None] = None
    role: UserRole = UserRole.LEARNER
    goal: UserGoal = UserGoal.LEARN_TO_SWIM

# Schema khi tạo user
class UserCreate(UserBase):
    password: str

# Schema đầy đủ khi trả về dữ liệu User
class User(UserBase):
    id: int
    created_at: datetime
    pools: List[Pool] = [] # Hiển thị danh sách hồ bơi mà user sở hữu

    class Config:
        from_attributes = True

# ---- Các schema Token giữ nguyên ----
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Union[str, None] = None