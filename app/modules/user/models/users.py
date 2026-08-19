from sqlalchemy import Column, Integer, String, DateTime, Text, Date
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_identity = Column(String(255), unique=True, index=True)
    user_type = Column(String(5), nullable=False)
    user_email = Column(String(255))
    user_full_name = Column(String(255))
    user_password = Column(String(255))
    user_mobile = Column(String(30), nullable=True)
    user_company_id = Column(Integer, nullable=True, default=None)
    user_office_id = Column(Integer, nullable=True, default=None)
    user_desk_id = Column(Integer, nullable=True, default=None)
    user_photo = Column(String(255), nullable=True)
    user_signature = Column(String(255), nullable=True)
    user_birthday = Column(Date, nullable=True)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
   