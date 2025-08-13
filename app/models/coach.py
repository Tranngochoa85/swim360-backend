from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class VerificationStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class CoachProfile(Base):
    __tablename__ = "coach_profiles"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    experience_summary = Column(String, nullable=True)
    specialties = Column(String, nullable=True) # Ví dụ: "Dạy trẻ em, Bơi bướm"
    video_url = Column(String, nullable=True)
    verification_status = Column(SQLAlchemyEnum(VerificationStatus), default=VerificationStatus.PENDING)

    # Mối quan hệ ngược lại với User
    user = relationship("User", back_populates="coach_profile")

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    document_url = Column(String, nullable=False)
    document_type = Column(String, default="certificate") # Ví dụ: 'certificate', 'id_card'

    # Mối quan hệ ngược lại với User
    user = relationship("User", back_populates="documents")