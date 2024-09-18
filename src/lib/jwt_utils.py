import jwt
import time
import os
from dotenv import load_dotenv

load_dotenv()

ISSUER = 'td:lc'

def create_token(user_id: str, data: dict, expiration: int = 60 * 60 * 24 * 7):

    iat = int(time.time())
    payload = {
        **data,
        'iat': iat,
        'exp': iat + expiration,
        'iss': ISSUER,
        'sub': user_id
    }

    token = jwt.encode(
        payload=payload, 
        key=os.getenv('SECRET_KEY'),
        headers={ 
        'typ': 'JWT',
        'alg': 'HS256'
    })

    return token
    

def decode_token(token: str) -> dict | None:

    payload = jwt.decode(
    jwt=token, 
    key=os.getenv('SECRET_KEY'),
    algorithms=['HS256'], 
    options={
        'require': ['exp', 'iat', 'iss', 'sub'],
        'verify_signature': True,
    }, 
    issuer=ISSUER)

    return payload