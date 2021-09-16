from unittest.mock import patch
from application.models.film import Film
from datetime import date

dummySlug = "matrix-1999"
    
test_film1 = Film()
test_film1.id = 1
test_film1.name = "Matrix 1999"
test_film1.description = 'matrix desc'
test_film1.fragman = "https://matrix.com/fragman"
test_film1.category_id = 1
test_film1.year = 1999
test_film1.cover = "https://pictures.com/matrix-1999"
test_film1.slug = dummySlug
test_film1.created_at = date.today()
test_film1.updated_at = date.today()

#Film.all()
@patch("application.models.film.Film")
def test_it_should_return_empty_array(mock_film):
    mock_film.query.all.return_value = []
    films = Film.all()

    assert(films == [])

#Film.all()
@patch("application.models.film.Film")
def test_it_should_return_films(mock_film):

    test_film2 = Film()
    test_film2.id = 1
    test_film2.name = "Matrix Reloaded"
    test_film2.description = "matrix reloaded desc"
    test_film2.fragman = "https://matrix-reloaded.com/fragman"
    test_film2.category_id = 1
    test_film2.year = 2003
    test_film2.cover = "https://pictures.com/matrix-reloaded"
    test_film2.slug = "matrix-reloaded"
    test_film2.created_at = date.today()
    test_film2.updated_at = date.today()

    excpected = [test_film1,test_film2]
    mock_film.query.all.return_value = excpected
    films = Film.all()

    assert(films == excpected)

#Film.get_by_slug()
@patch("application.models.film.Film")
def test_it_should_return_none(mock_film):
    mock_film.query.filter_by(slug=dummySlug).first.return_value = None
    film = Film.get_by_slug(dummySlug)

    assert(film == None)

#Film.get_by_slug()
@patch("application.models.film.Film")
def test_it_should_return_film(mock_film):
    mock_film.query.filter_by(slug=dummySlug).first.return_value = test_film1

    film = Film.get_by_slug(dummySlug)
    assert (film == test_film1)

#Film.to_json()
@patch("application.models.film.Film")
def test_it_should_return_film_json(mock_film):
    mock_film.query.filter_by(slug=dummySlug).first.return_value = test_film1
    film_json = Film.get_by_slug(dummySlug).to_json()

    film_dict = {
            'id': 1,
            'name': 'Matrix 1999',
            'description': 'matrix desc',
            'fragman': 'https://matrix.com/fragman',
            'cover': 'https://pictures.com/matrix-1999',
            'year': 1999,
            'category_id': 1,
            'slug': dummySlug,
            'created_at': date.today(),
            'updated_at': date.today()
        }

    assert (film_json == film_dict)
