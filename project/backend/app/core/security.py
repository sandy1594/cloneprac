 """
 Security utilities for password hashing and JWT handling.
 """

 from datetime import datetime, timedelta, timezone
 from typing import Any, Optional

 from jose import jwt
 from passlib.context import CryptContext

 from .config import settings

 pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


 def create_access_token(subject: str | Any, expires_delta: Optional[timedelta] = None) -> str:
     """
     Create a signed JWT access token for the given subject (user identifier).
     """
     if isinstance(subject, bytes):
         subject = subject.decode("utf-8")

     expires_delta = expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
     expire = datetime.now(timezone.utc) + expires_delta

     to_encode = {"sub": str(subject), "exp": expire}
     encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
     return encoded_jwt


 def verify_password(plain_password: str, hashed_password: str) -> bool:
     """Verify a plain password against a hashed password."""
     return pwd_context.verify(plain_password, hashed_password)


 def get_password_hash(password: str) -> str:
     """Hash a password for storage."""
     return pwd_context.hash(password)
