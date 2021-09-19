import requests
from application.services.film_service import FilmService
from unittest.mock import patch,Mock
from nose.tools import assert_dict_equal

films_response = {
    'films': [
        {
            'cover': 'https://matrix.com/cover.jpg',
            'created_at': 'Fri, 17 Sep 2021 19:39:57 GMT',
            'description': 'matrix desc',
            'fragman': 'https://w22ww.youtube.com/watch?v=c5gVlizVEQk',
            'genre_id': 1,
            'id': 1,
            'name': 'matrix 2',
            'slug': 'matrix-2',
            'updated_at': 'Fri, 17 Sep 2021 19:39:57 GMT',
            'year': 2100
        }
    ],
    'message': "successful",
    'status': True
}

genre_not_found = {
    "genre": None,
    "message": "genre not found",
    "status": False
}

films_not_found = {
    "films": None,
    "message": "there are no films",
    "status": False
}

dummy_film_service_response_data = {
    'status_code': 200,
    'response_data': films_response
}

dummy_film_service_genre_not_found_response_data = {
    'status_code': 404,
    'response_data': genre_not_found
}

dummy_film_service_films_not_found_response_data = {
    'status_code': 404,
    'response_data': films_not_found
}

@patch('application.services.film_service.requests.get')
def test_it_should_be_shown_films(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = films_response

    film_service_response = FilmService.get_films(1,'1')
    data = film_service_response['response_data']

    assert(film_service_response['status_code'] == 200)
    assert(len(data['films']) == 1)
    assert_dict_equal(film_service_response, dummy_film_service_response_data)

@patch('application.services.film_service.requests.get')
def test_it_should_be_genre_not_found_error(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = genre_not_found

    film_service_response = FilmService.get_films(1,'1')
    data = film_service_response['response_data']

    assert(film_service_response['status_code'] == 404)
    assert(data['genre'] is None)
    assert_dict_equal(film_service_response, dummy_film_service_genre_not_found_response_data)

@patch('application.services.film_service.requests.get')
def test_it_should_be_films_not_found_error(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = films_not_found

    film_service_response = FilmService.get_films(1,'1')
    data = film_service_response['response_data']

    assert(film_service_response['status_code'] == 404)
    assert(data['films'] is None)
    assert_dict_equal(film_service_response, dummy_film_service_films_not_found_response_data)
        


        