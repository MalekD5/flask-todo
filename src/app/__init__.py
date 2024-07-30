import os
from flask import (Flask, render_template)
from infrastructure import TodoRepository as td
from app.controller import todo_controller

app = Flask(__name__)

app.config["LIVETW_DEV"] = os.getenv("LIVETW_ENV") == "development"

app.register_blueprint(todo_controller.todo_bp)

@app.route('/')
def hello_world():
    return render_template('home.html', todos=td.get_todos())
