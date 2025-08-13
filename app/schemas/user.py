from pydantic import BaseModel
from datetime import datetime
from typing import Union, List
from app.models.user import UserRole, UserGoal
from .pool import Pool 

# Schema cơ bản, chứa các trường thông tin chung
class UserBase(BaseModel):
    email: str
    full_name: Union[str, None] = None
    role: UserRole
    goal: Union[UserGoal, None] = None

# Schema dùng khi tạo người dùng mới
class UserCreate(UserBase):
    password: str

# Schema dùng khi trả về dữ liệu người dùng từ API
class User(UserBase):
    id: int
    created_at: datetime
    pools: List[Pool] = [] # Hiển thị danh sách hồ bơi mà user sở hữu

    class Config:
        from_attributes = True

# Schema dùng khi Admin cập nhật role
class UserRoleUpdate(BaseModel):
    role: UserRole

# Schema cho Token
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema cho dữ liệu bên trong Token
class TokenData(BaseModel):
    email: Union[str, None] = None