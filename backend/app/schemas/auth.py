
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from pydantic import ConfigDict

# ---------- Request DTOs ----------

class RegisterRequest(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: Optional[str] = None
    email: EmailStr
    password: str = Field(..., min_length=8)   

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RefreshRequest(BaseModel):
    refresh_token: str


# ---------- Response DTOs ----------

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


    model_config = ConfigDict(from_attributes=True)


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    full_name: str                                

    model_config = ConfigDict(from_attributes=True)
