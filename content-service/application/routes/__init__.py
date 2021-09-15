from flask import Blueprint

content_service_api_blueprint = Blueprint('content_service_api', __name__)

from . import api