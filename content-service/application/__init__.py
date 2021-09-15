# application/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from os import environ
from redis import Redis

db = SQLAlchemy()
redis = Redis(host=environ['REDIS_HOST'], port=environ['REDIS_PORT'], db=0)
cache = Cache()

def create_app():
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ['SQLALCHEMY_DATABASE_URI']
    app.config['CACHE_TYPE'] = 'RedisCache'
    app.config['CACHE_REDIS_HOST'] = environ['REDIS_HOST']
    app.config['CACHE_REDIS_PORT'] = environ['REDIS_PORT']

    db.init_app(app)
    cache.init_app(app)

    with app.app_context():
        from .routes import content_service_api_blueprint
        app.register_blueprint(content_service_api_blueprint)


    return app



