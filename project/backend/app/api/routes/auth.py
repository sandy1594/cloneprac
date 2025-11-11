 """
 Authentication routes.
 """

 from fastapi import APIRouter, Depends, HTTPException, status
 from sqlalchemy.orm import Session

 from app.api import deps
 from app.core.security import create_access_token, get_password_hash
 from app.models.user import User
 from app.schemas import LoginRequest, Token, UserCreate, UserRead

 router = APIRouter()


 @router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
 def register_user(payload: UserCreate, db: Session = Depends(deps.get_db)) -> User:
     """Register a new patient or doctor user."""
     existing_user = deps.get_user_by_email(db, email=payload.email)
     if existing_user:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

     user = User(
         name=payload.name,
         email=payload.email,
         phone=payload.phone,
         role=payload.role,
         avatar_url=str(payload.avatar_url) if payload.avatar_url else None,
         hashed_password=get_password_hash(payload.password),
     )
     db.add(user)
     db.commit()
     db.refresh(user)
     return user


 @router.post("/login", response_model=Token)
 def login(payload: LoginRequest, db: Session = Depends(deps.get_db)) -> Token:
     """Authenticate user and issue access token."""
     user = deps.authenticate_user(db, email=payload.email, password=payload.password)
     if not user:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

     access_token = create_access_token(subject=user.email)
     return Token(access_token=access_token)


 @router.post("/verify", response_model=UserRead)
 def verify_token(current_user: User = Depends(deps.get_current_active_user)) -> User:
     """Return user info if token is valid."""
     return current_user
