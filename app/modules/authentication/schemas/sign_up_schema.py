from pydantic import BaseModel, EmailStr
from typing import Optional

class SignUpRequest(BaseModel):
    user_email : EmailStr
    password : str

class SignUpResponse(BaseModel):
    access_token : str
    token_type : str = "bearer"
    refresh_token : Optional[str] = None