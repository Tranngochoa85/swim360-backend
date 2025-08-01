from sqlalchemy import Column, Integer, String, DateTime, func, Enum as SQLAlchemyEnum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class UserRole(enum.Enum):
    LEARNER = "learner"
    COACH = "coach"
    POOL_OWNER = "pool_owner"
    ADMIN = "admin"

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

    pools = relationship("Pool", back_populates="owner", cascade="all, delete-orphan")
    
    # Mối quan hệ với Bookings
    bookings_as_learner = relationship("Booking", foreign_keys="[Booking.learner_id]", back_populates="learner")
    bookings_as_coach = relationship("Booking", foreign_keys="[Booking.coach_id]", back_populates="coach")