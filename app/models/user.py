from sqlalchemy import Column, Integer, String, DateTime, func, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

# Định nghĩa các vai trò của người dùng trong hệ thống
class UserRole(enum.Enum):
    LEARNER = "learner"
    COACH = "coach"
    POOL_OWNER = "pool_owner"
    ADMIN = "admin"

# Định nghĩa mục tiêu của người dùng khi tham gia
class UserGoal(enum.Enum):
    LEARN_TO_SWIM = "learn_to_swim"
    IMPROVE_SKILLS = "improve_skills"
    TRAIN_COMPETE = "train_compete"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False, default=UserRole.LEARNER)
    goal = Column(SQLAlchemyEnum(UserGoal), nullable=True, default=UserGoal.LEARN_TO_SWIM)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Một user (vai trò POOL_OWNER) có thể sở hữu nhiều hồ bơi
    pools = relationship("Pool", back_populates="owner", cascade="all, delete-orphan")