from marshmallow import Schema, fields, validate


class CreateUserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
