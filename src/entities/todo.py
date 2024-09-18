from dataclasses import dataclass

@dataclass
class Todo:
    id: str;
    text: str;
    completed: bool;

    @staticmethod
    def create(id, text, completed):
        return Todo(id, text, completed)

