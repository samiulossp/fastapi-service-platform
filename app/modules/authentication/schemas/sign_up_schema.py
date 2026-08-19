from pydantic import BaseModel
from typing import Optional

class SignUpRequest(BaseModel):
    user_identity : str
    password : str

class SignUpResponse(BaseModel):
    access_token : str
    token_type : str = "bearer"
    refresh_token : Optional[str] = None