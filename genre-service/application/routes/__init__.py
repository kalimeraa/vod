from flask import Blueprint

genre_service_api_blueprint = Blueprint('genre_service_api', __name__)

from . import api