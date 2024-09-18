import pytest
import jwt
import time
import os
from faker import Faker
from src.lib.jwt_utils import create_token, decode_token

def construct_token_payload(issuer: str):
    iat = int(time.time())
    payload = {
        'iat': iat,
        'exp': iat + 1000,
        'iss': issuer,
        'sub': 1
    }

    return payload

def test_jwt_create_token():
    token = create_token(1, {
        'role': 'admin'
    })

    decoded = decode_token(token)

    assert decoded is not None
    assert decoded['role'] == 'admin'
    assert decoded['sub'] == 1

def test_jwt_expiration():
    token = create_token(1, {
        'role': 'admin'
    }, expiration=0)

    with pytest.raises(Exception):
        decode_token(token)

def test_jwt_invalid_issuer():
    payload = construct_token_payload('fake:issuer')
    
    token = jwt.encode( payload=payload, key=os.getenv('SECRET_KEY'), headers={
        'typ': 'JWT',
        'alg': 'HS256'
    })

    with pytest.raises(jwt.exceptions.InvalidIssuerError):
        decode_token(token)

def test_jwt_invalid_signature(faker: Faker):
    payload = construct_token_payload('td:lc')

    token = jwt.encode(payload=payload, key=faker.password(length=8), headers={
        'typ': 'JWT',
        'alg': 'HS256'
    })

    with pytest.raises(jwt.exceptions.InvalidSignatureError):
        decode_token(token)

def test_jwt_invalid_algorithm():
    payload = construct_token_payload('td:lc')

    token = jwt.encode(payload=payload, key=os.getenv('SECRET_KEY'), algorithm='HS512', headers={'typ': 'JWT'})

    with pytest.raises(jwt.exceptions.InvalidAlgorithmError):
        decode_token(token)


def test_jwt_invalid_payload():
    token = jwt.encode(payload={
        'sub': 1
    }, key=os.getenv('SECRET_KEY'), algorithm='HS256', headers={'typ': 'JWT'})

    with pytest.raises(jwt.exceptions.MissingRequiredClaimError):
        decode_token(token)
