import requests
from os import environ
class FilmService():
    @staticmethod
    def get_films_by_slug(slug: str, page:str = '1'):
        response = requests.get(environ['CONTENT_SERVICE_ENDPOINT'] + '/genre/' + slug + '?page=' + page)
        
        return {'status_code':response.status_code,'response_data':response.json()}