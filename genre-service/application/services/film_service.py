import requests
from os import environ

class FilmService():
    @staticmethod
    def get_films(id: int, page:str = '1'):
        response = requests.get(environ['CONTENT_SERVICE_ENDPOINT'] + '/genre/' + str(id) + '?page=' + page)
        
        return {'status_code':response.status_code,'response_data':response.json()}