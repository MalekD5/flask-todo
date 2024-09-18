from src.infra.repository.user_repository import AbstractUserRepository, User
from bcrypt import checkpw

def login_usecase(user_repository: AbstractUserRepository, email: str, password: str):
    user = user_repository.get_user(email)

    if user is None:
        return False
    
    return checkpw(password, user.hashed_password)