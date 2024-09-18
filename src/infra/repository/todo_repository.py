from src.entities.todo import Todo

def get_todos() -> list[Todo]:
    return [
        Todo(1, "Buy milk", False),
        Todo(2, "Buy bread", False),
        Todo(3, "Buy eggs", False),
        Todo(4, "Buy cheese", False),
        Todo(5, "Buy butter", False),
        Todo(6, "Buy chocolate", False),
        Todo(7, "Buy sugar", False),
        Todo(8, "Buy coffee", False),
        Todo(9, "Buy tea", False),
        Todo(10, "Buy chocolate", False),
    ]

def add_todo(todo: Todo):
    pass

def delete_todo(todo: Todo):
    pass

def update_todo(todo: Todo):
    pass