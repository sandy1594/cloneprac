 """
 Common dependency functions for FastAPI routes.
 """

 from fastapi import Depends, HTTPException, status
 from fastapi.security import OAuth2PasswordBearer
 from jose import JWTError, jwt
 from sqlalchemy.orm import Session

 from app.core.config import settings
 from app.core.security import verify_password
 from app.db.session import SessionLocal
 from app.models.user import User

 oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_PREFIX}/auth/login")


 def get_db():
     """
     Provide a database session for request handling.
     """
     db = SessionLocal()
     try:
         yield db
     finally:
         db.close()


 def get_user_by_email(db: Session, email: str) -> User | None:
     """Retrieve a user by email."""
     return db.query(User).filter(User.email == email).first()


 def authenticate_user(db: Session, email: str, password: str) -> User | None:
     """Authenticate user credentials."""
     user = get_user_by_email(db, email=email)
     if not user or not verify_password(password, user.hashed_password):
         return None
     return user


 def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
     """Decode token and return the current user."""
     credentials_exception = HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail="Could not validate credentials",
         headers={"WWW-Authenticate": "Bearer"},
     )
     try:
         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
         email: str | None = payload.get("sub")
         if email is None:
             raise credentials_exception
     except JWTError as exc:  # pragma: no cover - narrow exception is logged elsewhere
         raise credentials_exception from exc

     user = get_user_by_email(db, email=email)
     if user is None:
         raise credentials_exception
     return user


 def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
     """
     Ensure the current user is enabled. Placeholder for additional checks.
     """
     if not current_user.is_active:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
     return current_user
