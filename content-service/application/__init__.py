# application/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgresrootuser:postgresrootpassword@content-db:5432/content-db"
    db.init_app(app)

    with app.app_context():
        from .routes import content_service_api_blueprint
        app.register_blueprint(content_service_api_blueprint)
        return app