from flask import Flask
from .routes import api_routes
from .api_blueprint import api_blueprint

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Register API routes
    app.register_blueprint(api_routes)

    return app