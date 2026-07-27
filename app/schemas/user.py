from pydantic import BaseModel, EmailStr, Field,ConfigDict

class UserCreate(BaseModel):
    name:str
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    
    
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# --- AUTH SCHEMAS ---
# Used for input validation when users login and to structure the JWT response.

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: EmailStr | None = None