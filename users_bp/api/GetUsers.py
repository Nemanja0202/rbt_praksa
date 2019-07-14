from app import db
from flask_restplus import Resource
from users_bp import users_api
from users_bp.models.Users import Users
from users_bp.schemas.GetUsersSchema import GetUsersSchema


@users_api.route("/latest", methods=['GET'])
class GetUsers(Resource):

    def get(self):
        data = db.session.query(Users)
        data = data[-1]
        get_schema = GetUsersSchema().dump(data)
        return get_schema
