from . import content_service_api_blueprint
from cerberus import Validator
from flask_accept import accept
from application.http.validations import film as film_schema
from flask import request,jsonify
from ..models.film import Film
from application import db
from slugify import slugify

v = Validator()

@content_service_api_blueprint.route('/api/films', methods=['POST'])
@accept('application/json')
def store():
    content = request.json
    
    v.validate(content,film_schema.create)
    if v.errors:
        return jsonify(v.errors),400

    film_exist = Film.getBySlug(slugify(content['name']))
    if film_exist is not None:
        return {'status':False,'message':'Film is already exist','film':film_exist.to_json()} ,409

    film = Film()
    film.name = content['name']
    film.cover = content['cover']
    film.fragman = content['fragman']
    film.description = content['description']
    film.year = content['year']
    film.category_id = content['category_id']
    
    db.session.add(film)
    db.session.commit()

    return {'status':True,'message':'created','film':film.to_json()}

@content_service_api_blueprint.route('/api/films/<string:slug>', methods=['PUT','PATCH'])
def update(slug):
    content = request.json
    content['slug'] = slug
    
    v.validate(content,film_schema.update)
    if v.errors:
        return jsonify(v.errors),400

    film_exist = Film.getBySlug(content['slug'])
    if film_exist is None:
        return {'status':False,'message':'film not found','film':None} ,404

    film_exist.name = content['name']
    film_exist.cover = content['cover']
    film_exist.fragman = content['fragman']
    film_exist.description = content['description']
    film_exist.year = content['year']
    film_exist.category_id = content['category_id']
    
    db.session.add(film_exist)
    db.session.commit()

    return {'status':True,'message':'updated','film':film_exist.to_json()}    

@content_service_api_blueprint.route('/api/films', methods=['GET'])
def index():
    films = Film.all()
    return jsonify({'status':True,'message':'successful','films':films})

@content_service_api_blueprint.route('/api/films/<string:slug>', methods=['GET'])
def show(slug):
    content = {'slug':slug}
    
    v.validate(content,film_schema.show)
    if v.errors:
        return jsonify(v.errors),400

    film_exist = Film.getBySlug(slug)
    if film_exist is None:
        return {'status':False,'message':'film not found','film':None} ,404

    return {'status':True,'message':'successful','film':film_exist.to_json()}

@content_service_api_blueprint.route('/api/films/<string:slug>', methods=['DELETE'])
def destroy(slug):
    content = {'slug':slug}
    
    v.validate(content,film_schema.delete)
    if v.errors:
        return jsonify(v.errors),400

    film_exist = Film.getBySlug(slug)
    if film_exist is None:
        return {'status':False,'message':'film not found','film':None} ,404

    film = Film.query.filter_by(slug=slug).one()
    db.session.delete(film)
    db.session.commit()

    return {'status':True,'message':'deleted','film':film}



    
 