import requests
from os import environ

class GenreService():

    @staticmethod
    def get_genre_by_id(id: int):
        response = requests.get(environ['GENRE_SERVICE_ENDPOINT'] + '/' + str(id))
        
        return {'status_code':response.status_code,'response_data':response.json()}