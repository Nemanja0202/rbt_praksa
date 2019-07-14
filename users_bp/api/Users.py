from app import db
from flask_restplus import Resource
from users_bp import users_api
from users_bp.models.Users import Users
from users_bp.schemas.CreateUsersSchema import CreateUsersSchema
from measurement_bp.api.Measurement import authentication_required

from flask import request


@users_api.route("/")
class CreateUsers(Resource):

    @authentication_required
    def post(self):
        data = request.get_json(force=True)

        validated_data = CreateUsersSchema().load(data)
        user = Users(username=data["username"], password=data["password"])
        db.session.add(user)
        db.session.commit()

        return {'message': 'User added'}, 200
