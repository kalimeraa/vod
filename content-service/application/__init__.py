# application/__init__.py
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from os import environ
from redis import Redis

db = SQLAlchemy()
redis = Redis(host=environ['REDIS_HOST'], port=environ['REDIS_PORT'], db=0)

def create_app(test=False):
    app = Flask(__name__)
    if test is True:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = environ['SQLALCHEMY_DATABASE_URI']

    app.config['CACHE_TYPE'] = 'RedisCache'
    app.config['CACHE_REDIS_HOST'] = environ['REDIS_HOST']
    app.config['CACHE_REDIS_PORT'] = environ['REDIS_PORT']
    
    db.init_app(app)

    with app.app_context():
        from .routes import content_service_api_blueprint
        app.register_blueprint(content_service_api_blueprint)
        
        #just migration
        if environ['FLASK_ENV'] == 'development':
            db.drop_all()
            db.create_all()
            
    return app



