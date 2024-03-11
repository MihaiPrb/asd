from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_db(app):
    db.init_app(app)
    app.app_context().push()
    create_tables()

def teardown_db(app):
    with app.app_context():
        drop_tables()
        db.session.remove()
        db.engine.dispose()