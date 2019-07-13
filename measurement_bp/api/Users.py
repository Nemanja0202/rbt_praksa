import os
from app import db
from flask_restplus import Resource
from measurement_bp import measurements_api
from app import Conf
from measurement_bp.models.Users import Users
from measurement_bp.schemas.CreateUsersSchema import CreateUserSchema
from measurement_bp.api.Measurement import Measurement, authentication_required
from marshmallow import ValidationError

from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request


@measurements_api.route("/users")
class CreateUsers(Resource):

    @authentication_required
    def post(self):
        data = request.get_json(force=True)

        validated_data = CreateUserSchema().load(data)
        user = Users(username=data["username"], password = data["password"])
        db.session.add(user)
        db.session.commit()


        return {'message': 'User added.'}, 200
