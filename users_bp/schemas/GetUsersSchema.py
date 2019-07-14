from marshmallow import Schema, fields


class GetUsersSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
