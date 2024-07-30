import os
from flask import (Flask, render_template)
from infrastructure import TodoRepository as td
from app.routes import todo_routes
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()

login_manager.init_app(app)

app.config["LIVETW_DEV"] = os.getenv("LIVETW_ENV") == "development"

app.register_blueprint(todo_routes.todo_bp)

@app.route('/')
def hello_world():
    return render_template('home.html', todos=td.get_todos())
