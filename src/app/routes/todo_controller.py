from flask import Blueprint, get_template_attribute
import random

todo_bp = Blueprint('todo', __name__, url_prefix='/todos')

@todo_bp.route('/')
def get_todo():
    todoId = str(random.randint(1, 10000))
    data = {
        "id": "testTodo" + todoId,
        "text": f"Test todo {todoId}",
        "completed": False
    }

    template = get_template_attribute('components/todo-item.html', 'todoItem')

    return template(id=data.get('id'), text=data.get('text'))
