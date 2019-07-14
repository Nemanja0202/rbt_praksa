from marshmallow import Schema, fields


class CreateUsersSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
