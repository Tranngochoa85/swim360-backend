from pydantic import BaseModel
from typing import Union, List
from app.models.coach import VerificationStatus

# --- Document Schemas ---
class DocumentBase(BaseModel):
    document_url: str
    document_type: str = "certificate"

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True

# --- CoachProfile Schemas ---
class CoachProfileBase(BaseModel):
    experience_summary: Union[str, None] = None
    specialties: Union[str, None] = None
    video_url: Union[str, None] = None

class CoachProfileCreate(CoachProfileBase):
    pass

class CoachProfileUpdate(CoachProfileBase):
    pass

class CoachProfile(CoachProfileBase):
    user_id: int
    verification_status: VerificationStatus
    documents: List[Document] = [] # Hiển thị danh sách chứng chỉ
    class Config:
        from_attributes = True