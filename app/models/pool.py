from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

# Định nghĩa các trạng thái của hồ bơi
class PoolStatus(enum.Enum):
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"

class Pool(Base):
    __tablename__ = "pools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    pool_type = Column(String, nullable=True)
    operating_hours = Column(String, nullable=True)

    # Dùng JSON để lưu cấu trúc giá vé linh hoạt
    fee_structure = Column(JSON, nullable=True) 

    policy_for_coaches = Column(String, nullable=True)
    status = Column(SQLAlchemyEnum(PoolStatus), default=PoolStatus.PENDING_APPROVAL)

    # Liên kết hồ bơi này với người sở hữu nó
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="pools")