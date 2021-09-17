import requests
from os import environ

class GenreService():

    @staticmethod
    def get_genre_by_slug(slug: str):
        response = requests.get(environ['GENRE_SERVICE_ENDPOINT'] + '/' + slug)
        
        return {'status_code':response.status_code,'response_data':response.json()}