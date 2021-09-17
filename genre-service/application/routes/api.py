from . import genre_service_api_blueprint
from cerberus import Validator
from application.http.validations import genre as genre_schema
from flask import request,jsonify
from ..models.genre import Genre
from ..services.redis_service import store_genre_detail,get_genre_detail,store_genres_page,get_genres_page
from ..services.film_service import FilmService
from .. import db
from slugify import slugify
import json

v = Validator()

@genre_service_api_blueprint.route('/api/genres', methods=['POST'])
def store():
    input = request.json
    v.validate(input,genre_schema.create)
    if v.errors:
        return jsonify(v.errors),400

    genre = Genre.get_by_slug(slugify(input['name']))
    if genre is not None:
        return {'status':False,'message':'genre is already exist','genre':genre.to_json()},409

    genre = Genre.create(input)
    
    return {'status':True,'message':'created','genre':genre.to_json()}

@genre_service_api_blueprint.route('/api/genres/<string:slug>', methods=['PUT','PATCH'])
def update(slug):
    input = request.json
    v.validate(input,genre_schema.update)
    if v.errors:
        return jsonify(v.errors),400
    
    genre = Genre.get_by_slug(slug)
    if genre is None:
        return {'status':False,'message':'genre not found','genre':None},404

    genre = genre.update(input)

    return {'status':True,'message':'updated','genre':genre.to_json()}    

@genre_service_api_blueprint.route('/api/genres', methods=['GET'])
def index():
    page_size=20
    pageArg = request.args.get('page')
    if pageArg is None:
        page = 1
    else:
        page = int(pageArg)
    
    redis_genres_page = get_genres_page(page)
    if redis_genres_page is not None:
        genres = json.loads(redis_genres_page)

        return jsonify(genres)
    
    genres = Genre.query.limit(page_size).offset(page-1**page_size).all()
    if len(genres) == 0:
        return {'status':False,'message':'there are no genres','genres':None},404
    
    response = jsonify({'status':True,'message':'successful','genres':genres})

    store_genres_page(page,response.get_data())
    
    return response

@genre_service_api_blueprint.route('/api/genres/<string:slug>', methods=['GET'])
def show(slug):
    redis_genre_detail = get_genre_detail(slug)    
    if redis_genre_detail is not None:
        genre = json.loads(redis_genre_detail)
        return jsonify(genre)

    genre = Genre.get_by_slug(slug)
    if genre is None:
        return {'status':False,'message':'genre not found','genre':None},404
        
    response = jsonify({'status':True,'message':'successful','genre':genre.to_json()})
    
    store_genre_detail(slug,response.get_data())

    return response

@genre_service_api_blueprint.route('/api/genres/<string:slug>', methods=['DELETE'])
def destroy(slug):
    genre = Genre.get_by_slug(slug)
    if genre is None:
        return {'status':False,'message':'genre not found','genre':None},404

    genre.delete()

    return {'status':True,'message':'deleted','genre':genre}

@genre_service_api_blueprint.route('/api/genres/<string:slug>/films', methods=['GET'])
def show_films(slug):
    pageArg = request.args.get('page')
    if pageArg is None:
        page = '1'
    else:
        page = pageArg

    genre = Genre.get_by_slug(slug)
    if genre is None:
        return {'status':False,'message':'genre not found','genre':None},404

    """
        1) Don't cache bcs if film name had changed you wouldn't have seen that changes on redis cache response and content service already caches it
        2) With Observer pattern on every delete,update and create actions flusing genre based redis caches Just check film_observer.py at content-service project
    """
    
    response = FilmService.get_films_by_slug(slug,page)
    #return response
    return response['response_data'], response['status_code']
    
    