from pydantic import (BaseModel, AfterValidator, field_validator)
from typing_extensions import Annotated
from validator_collection import email, has_length

class LoginRequestModel(BaseModel):
    email: str
    password: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        return email(v, allow_empty=False)
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if has_length(v, minimum=8, maximum=32) and ' ' not in v: 
            return v
        
        raise ValueError('Password must be between 8 and 32 characters long')
