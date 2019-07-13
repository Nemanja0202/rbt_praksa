from marshmallow import Schema, fields


class GetMeasurementSchema(Schema):
    id = fields.Integer(required=True)
    air_quality = fields.Float(required=True)
    temperature = fields.Float(required=True)
    humidity = fields.Float(required=True)
    time_stamp = fields.DateTime(required=True)