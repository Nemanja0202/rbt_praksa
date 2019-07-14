from marshmallow import Schema, fields, validate


class CreateMeasurementSchema(Schema):
    air_quality = fields.Float(required=True, validate=validate.Range(min=0, max=50))
    temperature = fields.Float(required=True, validate=validate.Range(min=-100, max=100))
    humidity = fields.Float(required=True, validate=validate.Range(min=0, max=100))
