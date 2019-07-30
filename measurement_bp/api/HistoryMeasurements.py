import math

from datetime import datetime
from app import db
from flask_restplus import Resource
from measurement_bp import measurements_api
from measurement_bp.models.Measurement import Measurement
from measurement_bp.schemas.GetMeasurementSchema import GetMeasurementSchema


@measurements_api.route("/history/<int:start_date>/<int:end_date>/<int:limit>/", methods=['GET'])
class HistoryMeasurement(Resource):

    def get(self, start_date, end_date, limit):
        start_date_format = datetime.fromtimestamp(start_date)
        end_date_format = datetime.fromtimestamp(end_date)

        data = db.session.query(Measurement).filter(Measurement.time_stamp > start_date_format, Measurement.time_stamp < end_date_format).all()
        get_schema = GetMeasurementSchema(many=True).dump(data)
        step = math.ceil(len(data) / limit)
        return get_schema[::-step]
