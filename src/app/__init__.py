import os
from flask import (Flask, render_template)
from src.app.routes import auth_routes, todo_routes
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.secret_key = os.getenv("SECRET_KEY")

    app.config["LIVETW_DEV"] = os.getenv("LIVETW_ENV") == "development"

    app.register_blueprint(todo_routes.todo_bp)
    app.register_blueprint(auth_routes.auth_bp)

    return app
