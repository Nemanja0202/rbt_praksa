from app import db
from flask_restplus import Resource
from measurement_bp import measurements_api
from measurement_bp.models.Measurement import Measurement
from measurement_bp.schemas.GetMeasurementSchema import GetMeasurementSchema


@measurements_api.route("/latest", methods=['GET'])
class GetMeasurement(Resource):

    def get(self):
        data = db.session.query(Measurement).all()
        data = data[-1]
        get_schema = GetMeasurementSchema().dump(data)
        return get_schema
