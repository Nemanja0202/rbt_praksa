from flask import Blueprint
from flask_restplus import Api
from marshmallow import ValidationError

users_bp = Blueprint('users', __name__, url_prefix="/users")

users_api = Api(users_bp)


@users_api.errorhandler(ValidationError)
def _handle_api_error(ex):
    return "Hell"


from users_bp.api.Users import Users
from users_bp.api.GetUsers import GetUsers
