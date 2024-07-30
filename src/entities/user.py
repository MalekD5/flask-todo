from dataclasses import dataclass

@dataclass
class User:
    id: str;
    name: str;
    email: str;

    @staticmethod
    def create(id, name, email):
        return User(id, name, email)