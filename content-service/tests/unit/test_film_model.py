from unittest.mock import patch,MagicMock
from application.models.film import Film
from datetime import date
import sqlalchemy 
 
dummySlug = "matrix-1999"
    
test_film1 = Film()
test_film1.id = 1
test_film1.name = "Matrix 1999"
test_film1.description = 'matrix desc'
test_film1.fragman = "https://matrix.com/fragman"
test_film1.genre_id = 1
test_film1.year = 1999
test_film1.cover = "https://pictures.com/matrix-1999"
test_film1.slug = dummySlug
test_film1.created_at = date.today()
test_film1.updated_at = date.today()

#Film.all()
@patch("application.models.film.Film")
def test_should_be_returned_empty_array(mock_film):
    mock_film.query.all.return_value = []
    films = Film.all()

    assert(films == [])

#Film.all()
@patch("application.models.film.Film")
def test_should_be_returned_films(mock_film):
    test_film2 = Film()
    test_film2.id = 1
    test_film2.name = "Matrix Reloaded"
    test_film2.description = "matrix reloaded desc"
    test_film2.fragman = "https://matrix-reloaded.com/fragman"
    test_film2.genre_id = 1
    test_film2.year = 2003
    test_film2.cover = "https://pictures.com/matrix-reloaded"
    test_film2.slug = "matrix-reloaded"
    test_film2.created_at = date.today()
    test_film2.updated_at = date.today()

    expected = [test_film1,test_film2]
    mock_film.query.all.return_value = expected
    films = Film.all()

    assert(films == expected)

#Film.get_by_slug()
@patch("application.models.film.Film")
def test_should_be_returned_none(mock_film):
    mock_film.query.filter_by(slug=dummySlug).first.return_value = None
    film = Film.get_by_slug(dummySlug)

    assert(film == None)

#Film.get_by_slug()
@patch("application.models.film.Film")
def test_should_be_returned_film_by_slug(mock_film):
    mock_film.query.filter_by(slug=dummySlug).first.return_value = test_film1

    film = Film.get_by_slug(dummySlug)
    assert (film == test_film1)

#Film.get_by_id()
@patch("application.models.film.Film")
def test_should_be_returned_film_by_id(mock_film):
    mock_film.query.filter_by(id=1).first.return_value = test_film1

    film = Film.get_by_id(1)
    assert (film == test_film1)

#Film.to_json()
@patch("application.models.film.Film")
def test_should_be_returned_film_json(mock_film):
    mock_film.query.filter_by(slug=dummySlug).first.return_value = test_film1
    film_json = Film.get_by_slug(dummySlug).to_json()

    film_dict = {
            'id': 1,
            'name': 'Matrix 1999',
            'description': 'matrix desc',
            'fragman': 'https://matrix.com/fragman',
            'cover': 'https://pictures.com/matrix-1999',
            'year': 1999,
            'genre_id': 1,
            'slug': dummySlug,
            'created_at': date.today(),
            'updated_at': date.today()
        }

    assert (film_json == film_dict)

#Film.delete()
@patch("application.models.film.Film")
def test_should_be_deleted_film(mock_film):
    mock_film.query.filter_by(slug=dummySlug).first.return_value = test_film1
    
    film = Film.get_by_slug(dummySlug)
    
    patched_delete = MagicMock(spec=sqlalchemy.orm.Session.delete)
    patched_commit = MagicMock(spec=sqlalchemy.orm.Session.commit)
    
    with patch('application.db.session.delete', new=patched_delete):
        with patch('application.db.session.commit', new=patched_commit):
            status = film.delete()    
            assert(status == True)

#Film.create()
def test_should_be_created_film():
    data = {
            'name': 'Matrix 1999',
            'description': 'matrix desc',
            'fragman': 'https://matrix.com/fragman',
            'cover': 'https://pictures.com/matrix-1999',
            'year': 1999,
            'genre_id': 1,
    }
    
    patched_add = MagicMock(spec=sqlalchemy.orm.Session.add)
    patched_commit = MagicMock(spec=sqlalchemy.orm.Session.commit)
    
    with patch('application.db.session.add', new=patched_add):
        with patch('application.db.session.commit', new=patched_commit):
            film = Film.create(data)
            
            film.id = 1
            film.slug = 'matrix-1999'
            film.created_at = date.today()
            test_film1.updated_at = None
            
            assert (film == test_film1)
    
    
#Film.update()
@patch("application.models.film.Film")
def test_should_be_updated_film(mock_film):
    mock_film.query.filter_by(slug=dummySlug).first.return_value = test_film1  
    patched_add = MagicMock(spec=sqlalchemy.orm.Session.add)
    patched_commit = MagicMock(spec=sqlalchemy.orm.Session.commit)

    expected_year = 3333
    data = {
            'name': 'Matrix 1999',
            'description': 'matrix desc',
            'fragman': 'https://matrix.com/fragman',
            'cover': 'https://pictures.com/matrix-1999',
            'year': expected_year,
            'genre_id': 1,
    }
    
    with patch('application.db.session.add', new=patched_add):
        with patch('application.db.session.commit', new=patched_commit):
            film = Film.get_by_slug(dummySlug)
            updated_film = film.update(data)

            assert (updated_film.year == expected_year)    