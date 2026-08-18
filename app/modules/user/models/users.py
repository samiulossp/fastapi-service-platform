from sqlalchemy import Column, Integer, String, DateTime, Text, Date
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_identity = Column(String, unique=True, index=True)
    user_type = Column(String(10), nullable=False)
    user_email = Column(String)
    user_full_name = Column(String)
    user_password = Column(String)
    user_mobile = Column(String(20), nullable=True)
    user_company_id = Column(Integer, nullable=True, default=None)
    user_office_id = Column(Integer, nullable=True, default=None)
    user_desk_id = Column(Integer, nullable=True, default=None)
    user_photo = Column(Text, nullable=False)
    user_signature = Column(Text, nullable=False)
    user_birthday = Column(Date, nullable=True)
    created_at = Column(DateTime, nullable=True)
    created_by = Column(Integer, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    updated_by = Column(Integer, nullable=True)