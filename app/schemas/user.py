from pydantic import BaseModel
from datetime import datetime
from typing import Union

# Schema cơ bản, chứa các trường thông tin chung
class UserBase(BaseModel):
    email: str
    full_name: Union[str, None] = None
    role: str = 'learner'

# Schema dùng khi tạo người dùng mới (dữ liệu từ request)
class UserCreate(UserBase):
    password: str

# Schema dùng khi trả về dữ liệu người dùng (dữ liệu trong response)
class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Schema cho Token
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema cho dữ liệu bên trong Token
class TokenData(BaseModel):
    email: Union[str, None] = None