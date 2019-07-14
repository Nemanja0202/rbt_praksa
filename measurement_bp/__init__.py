from flask import Blueprint
from flask_restplus import Api
from marshmallow import ValidationError

measurements_bp = Blueprint('measurement', __name__, url_prefix="/measurements")

measurements_api = Api(measurements_bp)


@measurements_api.errorhandler(ValidationError)
def _handle_api_error(ex):
    return "Hell"


from measurement_bp.api.Measurement import Measurements
from measurement_bp.api.GetMeasurement import GetMeasurement
