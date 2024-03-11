from flask import Flask
from config import Config
from api import api_blueprint
from database import db
from utils.logger import setup_logger
from utils.handle_exceptions import handle_exceptions
import streamlit as st
from user_interface import main as run_streamlit_app

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register API blueprint
app.register_blueprint(api_blueprint)

# Setup logger
setup_logger(app)

# Register error handlers
handle_exceptions(app)


@app.route('/')
def index():
    return 'Welcome to the Supply Chain Optimization Backend!'


def run_flask_app():
    with app.app_context():
        # Create database tables
        db.create_all()

    app.run(debug=True)


if __name__ == '__main__':
    # Run the Flask app and Streamlit app concurrently
    import threading

    flask_thread = threading.Thread(target=run_flask_app)
    streamlit_thread = threading.Thread(target=run_streamlit_app)

    flask_thread.start()
    streamlit_thread.start()

    flask_thread.join()
    streamlit_thread.join()