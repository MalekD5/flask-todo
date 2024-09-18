from flask import Blueprint, request
from src.port.schema.login_schema import LoginRequestModel
from pydantic import ValidationError
from src.infra.repository import user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    json = request.get_json()

    try:
        data = LoginRequestModel.model_validate(json)
    except ValidationError as e:
        print(e)

        return "Invalid data", 400
    

    return data.model_dump()

@auth_bp.route("/register", methods=["POST"])
def register():
    json = request.get_json()

    
