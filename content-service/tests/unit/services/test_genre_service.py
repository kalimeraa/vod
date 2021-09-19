import requests
from application.services.genre_service import GenreService
from unittest.mock import patch,Mock
from nose.tools import assert_dict_equal

genre_not_found = {
    "genre": None,
    "message": "genre not found",
    "status": False
}

genre_reponse = {
    "genre": {
        "cover": "https://www.imdb.pic/horror.jpg",
        "created_at": "Sun, 19 Sep 2021 14:43:50 GMT",
        "description": "horror movies",
        "id": 1,
        "name": "horror",
        "slug": "horror",
        "updated_at": "Sun, 19 Sep 2021 14:43:50 GMT"
    },
    "message": "created",
    "status": True
}

dummy_genre_service_response_data = {
    'status_code': 200,
    'response_data': genre_reponse
}

dummy_genre_service_genre_not_found_response_data = {
    'status_code': 404,
    'response_data': genre_not_found
}

@patch('application.services.genre_service.requests.get')
def test_it_should_be_shown_genre(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = genre_reponse

    genre_service_response = GenreService.get_genre_by_id(1)
    data = genre_service_response['response_data']

    assert(genre_service_response['status_code'] == 200)
    assert(data['genre'] is not None)
    assert_dict_equal(genre_service_response, dummy_genre_service_response_data)

@patch('application.services.genre_service.requests.get')
def test_it_should_be_genre_not_found_error(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = genre_not_found

    genre_service_response = GenreService.get_genre_by_id(1)
    data = genre_service_response['response_data']

    assert(genre_service_response['status_code'] == 404)
    assert(data['genre'] is None)
    assert_dict_equal(genre_service_response, dummy_genre_service_genre_not_found_response_data)
        


        