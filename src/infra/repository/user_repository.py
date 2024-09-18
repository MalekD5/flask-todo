from typing_extensions import override
from src.port.repository.abstract_user_repository import AbstractUserRepository
from src.database import engine
from src.database.schemas import User
from sqlalchemy.orm import Session
from sqlalchemy import select

class UserRepository(AbstractUserRepository):
    @override
    def get_user(self, user_email: str) -> User | None:
        user = None
        with Session(engine) as session:
            stmt = select(User).where(User.email == user_email)

            user = session.scalars(stmt).first()

        return user

    @override
    def create_user(self, user: User):
        pass
    