 """
 Authentication request schemas.
 """

 from pydantic import BaseModel, EmailStr


 class LoginRequest(BaseModel):
     """User login payload."""

     email: EmailStr
     password: str
