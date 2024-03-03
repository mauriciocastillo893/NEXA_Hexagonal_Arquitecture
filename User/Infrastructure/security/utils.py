from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from flask_jwt_extended import create_access_token as flask_create_access_token
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()

def configure_jwt(app):
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') 
    jwt = JWTManager(app)

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') 
JWT_REFRESH_SECRET_KEY = os.getenv('WT_REFRESH_SECRET_KEY')

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)




def create_custom_access_token(subject: Union[str, Any], user_role: str, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject), "type": user_role}
    encoded_jwt = flask_create_access_token(identity=to_encode)
    return encoded_jwt