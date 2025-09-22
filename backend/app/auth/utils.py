from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config import Settings

settings = Settings()

# password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    '''Hash plain password using bcrypt.'''
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    '''Verify plain password against hashed password.'''
    return pwd_context.verify(plain_password,hashed_password)


# JWT setup

SECRET_KEY =                    settings.JWT_SECRET_KEY
ALGORITHM =                     settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES =   settings.JWT_ACCESS_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS =     settings.JWT_REFRESH_EXPIRE_DAYS

def create_access_token(data:dict, expires_delta:Optional[timedelta]= None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def decode_access_token(token:str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    
def create_refresh_token(data:dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
