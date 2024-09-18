from dataclasses import dataclass
from flask_login import UserMixin

@dataclass
class User(UserMixin):
    id: str;
    name: str;
    email: str;

    @staticmethod
    def create(id, name, email):
        return User(id, name, email)
