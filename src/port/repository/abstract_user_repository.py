from abc import abstractmethod
from src.database.schemas import User

class AbstractUserRepository:
    @abstractmethod
    def get_user(self, user_email: str) -> User | None:
        pass

    @abstractmethod
    def create_user(self, user: User):
        pass


