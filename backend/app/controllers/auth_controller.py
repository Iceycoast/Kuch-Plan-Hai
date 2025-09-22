from sqlalchemy.orm import Session
from app.models import User
from app.auth.utils import (decode_access_token, 
                            hash_password, 
                            verify_password, 
                            create_access_token, 
                            create_refresh_token)

def register_user(db: Session, first_name: str, last_name: str | None, email: str, password: str):

    if db.query(User).filter(User.email == email).first():
        return None, "Email already registered"

    user = User(first_name=first_name, last_name=last_name, email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)

    tokens = issue_tokens(user)
    return (user, tokens), None


def login_user(db:Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        return None, "Invalid Credentials"

    tokens = issue_tokens(user)
    return (user, tokens), None


def refresh_tokens(db: Session, user_id: int):

    user = db.get(User, user_id)

    if not user:
        return None, "User not found"

    return issue_tokens(user), None


def issue_tokens(user: User):
    
    subject = {"sub": str(user.id), "email": user.email}

    return{
        "access_token": create_access_token(subject),
        "refresh_token": create_refresh_token(subject),
        "token_type": "bearer",
    }


def get_current_user(db:Session, token: str) -> User:
    """Get current user from JWT token"""

    data = decode_access_token(token)

    if not data or "sub" not in data:
        return None, "Invalid or expired token"

    user = db.get(User, int(data["sub"]))

    if not user: 
        return None, "User not found"

    return user, None