from . import content_service_api_blueprint
from cerberus import Validator
from application.http.validations import film as film_schema
from flask import request,jsonify
from ..models.film import Film
from ..services.redis_service import store_film_detail,get_film_detail,store_films_page,get_films_page
from .. import db
from slugify import slugify
import json

v = Validator()

@content_service_api_blueprint.route('/api/films', methods=['POST'])
def store():
    input = request.json
    v.validate(input,film_schema.create)
    if v.errors:
        return jsonify(v.errors),400

    film = Film.get_by_slug(slugify(input['name']))
    if film is not None:
        return {'status':False,'message':'film is already exist','film':film.to_json()},409

    film = Film.create(input)
    
    return {'status':True,'message':'created','film':film.to_json()}

@content_service_api_blueprint.route('/api/films/<string:slug>', methods=['PUT','PATCH'])
def update(slug):
    input = request.json
    v.validate(input,film_schema.update)
    if v.errors:
        return jsonify(v.errors),400
    
    film = Film.get_by_slug(slug)
    if film is None:
        return {'status':False,'message':'film not found','film':None},404

    film = film.update(input)

    return {'status':True,'message':'updated','film':film.to_json()}    

@content_service_api_blueprint.route('/api/films', methods=['GET'])
def index():
    page_size=20
    pageArg = request.args.get('page')
    if pageArg is None:
        page = 1
    else:
        page = int(pageArg)
    
    redis_films_page = get_films_page(page)
    if redis_films_page is not None:
        films = json.loads(redis_films_page)

        return jsonify(films)
    
    films = Film.query.limit(page_size).offset(page-1**page_size).all()
    if len(films) == 0:
        return {'status':False,'message':'there are no films','films':None},404
    
    response = jsonify({'status':True,'message':'successful','films':films})

    store_films_page(page,response.get_data())
    
    return response

@content_service_api_blueprint.route('/api/films/<string:slug>', methods=['GET'])
def show(slug):
    input = {'slug':slug}
    v.validate(input,film_schema.show)
    if v.errors:
        return jsonify(v.errors),400

    redis_film_detail = get_film_detail(slug)    
    if redis_film_detail is not None:
        films = json.loads(redis_film_detail)

        return jsonify(films)

    film = Film.get_by_slug(slug)
    if film is None:
        return {'status':False,'message':'film not found','film':None},404
        
    response = jsonify({'status':True,'message':'successful','film':film.to_json()})
    
    store_film_detail(slug,response.get_data())

    return response

@content_service_api_blueprint.route('/api/films/<string:slug>', methods=['DELETE'])
def destroy(slug):
    input = {'slug':slug}
    
    v.validate(input,film_schema.delete)
    if v.errors:
        return jsonify(v.errors),400

    film = Film.get_by_slug(slug)
    if film is None:
        return {'status':False,'message':'film not found','film':None},404

    film.delete()

    return {'status':True,'message':'deleted','film':film}



    
 