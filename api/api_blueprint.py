# api/api_blueprint.py

from flask import Blueprint
from .routes import api_routes

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Register the API routes
api_blueprint.register_blueprint(api_routes)