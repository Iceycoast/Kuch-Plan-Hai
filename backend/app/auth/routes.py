from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from typing import Optional


from app.db import get_db
from app.models import User
from app.controllers.auth_controller import(    get_current_user,
                                                register_user,
                                                login_user,
                                                refresh_tokens
)
from app.auth.utils import decode_access_token
from app.schemas.auth import(   RegisterRequest,
                                LoginRequest,
                                RefreshRequest,
                                TokenResponse,
                                UserOut
)


router = APIRouter()

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):

    '''Register a new user with first name, last name(optional), email, and password.'''

    result, err = register_user(
                                db = db,
                                first_name= payload.first_name,
                                last_name= payload.last_name,
                                email=payload.email,
                                password=payload.password
    )

    if err:
        if "Email already registered" in err.lower():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=err)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err)
    
    user, tokens = result 
    return tokens 


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):

    '''Login with email and password, returns access and refrest tokens.'''
    
    result, err = login_user(
                                db = db,
                                email= payload.email,
                                password= payload.password
    )   

    if err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=err)

    user, tokens = result
    return tokens

@router.post("/refresh", response_model=TokenResponse)
def refresh(payload: RefreshRequest, db: Session = Depends(get_db)):

    '''Refresh access tokens using refresh token.'''

    data = decode_access_token(payload.refresh_token)

    if not data or "sub" not in data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    tokens, err = refresh_tokens(db = db, user_id= int(data["sub"]))

    if err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=err)

    return tokens 

def get_current_user_dependency(authorization: Optional[str] = Header(default=None), db: Session = Depends(get_db)) -> User:

    '''FastAPI dependency wrapper for get_current_user.'''

    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid authorization header")

    token = authorization.split(" ", 1)[1]
    user, err = get_current_user(db=db, token=token)

    if err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=err)

    return user

@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user_dependency)):

    '''Get current user profile.'''

    return UserOut(
                    id = current_user.id,
                    first_name= current_user.first_name,
                    last_name= current_user.last_name,
                    email= current_user.email,
                    full_name= current_user.full_name

    )