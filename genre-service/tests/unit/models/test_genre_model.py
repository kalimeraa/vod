from unittest.mock import patch,MagicMock
from application.models.genre import Genre
from datetime import date
import sqlalchemy 
 
dummy_slug = "horror"
dummy_id = 1
    
test_genre1 = Genre()
test_genre1.id = 1
test_genre1.name = "Horror"
test_genre1.description = 'horror movies'
test_genre1.cover = "https://pictures.com/horror-cover.jpg"
test_genre1.slug = dummy_slug
test_genre1.created_at = date.today()
test_genre1.updated_at = date.today()

#genre.all()
@patch("application.models.genre.Genre")
def test_should_be_returned_empty_array(mock_genre):
    mock_genre.query.all.return_value = []
    genres = Genre.all()

    assert(genres == [])

#genre.all()
@patch("application.models.genre.Genre")
def test_should_be_returned_genres(mock_genre):
    test_genre2 = Genre()
    test_genre2.id = 1
    test_genre2.name = "Fiction"
    test_genre2.description = "fiction movies"
    test_genre2.cover = "https://pictures.com/fiction-cover.jpg"
    test_genre2.slug = "fiction"
    test_genre2.created_at = date.today()
    test_genre2.updated_at = date.today()

    expected = [test_genre1,test_genre2]
    mock_genre.query.all.return_value = expected
    genres = Genre.all()

    assert(genres == expected)

#genre.get_by_slug()
@patch("application.models.genre.Genre")
def test_should_be_returned_none(mock_genre):
    mock_genre.query.filter_by(slug=dummy_slug).first.return_value = None
    genre = Genre.get_by_slug(dummy_slug)

    assert(genre == None)

#genre.get_by_id()
@patch("application.models.genre.Genre")
def test_should_be_returned_genre_by_id(mock_genre):
    mock_genre.query.filter_by(id=dummy_id).first.return_value = test_genre1

    genre = Genre.get_by_id(dummy_id)
    assert (genre == test_genre1)

#genre.get_by_slug()
@patch("application.models.genre.Genre")
def test_should_be_returned_genre_by_slug(mock_genre):
    mock_genre.query.filter_by(slug=dummy_slug).first.return_value = test_genre1

    genre = Genre.get_by_slug(dummy_slug)
    assert (genre == test_genre1)

#genre.to_json()
@patch("application.models.genre.Genre")
def test_should_be_returned_genre_json(mock_genre):
    mock_genre.query.filter_by(slug=dummy_slug).first.return_value = test_genre1
    genre_json = Genre.get_by_slug(dummy_slug).to_json()

    genre_dict = {
            'id': 1,
            'name': 'Horror',
            'description': 'horror movies',
            'cover': 'https://pictures.com/horror-cover.jpg',
            'slug': dummy_slug,
            'created_at': date.today(),
            'updated_at': date.today()
        }

    assert (genre_json == genre_dict)

#genre.delete()
@patch("application.models.genre.Genre")
def test_should_be_deleted_genre(mock_genre):
    mock_genre.query.filter_by(slug=dummy_slug).first.return_value = test_genre1
    
    genre = Genre.get_by_slug(dummy_slug)
    
    patched_delete = MagicMock(spec=sqlalchemy.orm.Session.delete)
    patched_commit = MagicMock(spec=sqlalchemy.orm.Session.commit)
    
    with patch('application.db.session.delete', new=patched_delete):
        with patch('application.db.session.commit', new=patched_commit):
            status = genre.delete()

            assert(status == True)

#genre.create()
def test_should_be_created_genre():
    data = {
            'name': 'Horror',
            'description': 'horror movies',
            'cover': 'https://pictures.com/horror-cover.jpg',
    }
    
    patched_add = MagicMock(spec=sqlalchemy.orm.Session.add)
    patched_commit = MagicMock(spec=sqlalchemy.orm.Session.commit)
    
    with patch('application.db.session.add', new=patched_add):
        with patch('application.db.session.commit', new=patched_commit):
            genre = Genre.create(data)
            
            genre.id = 1
            genre.slug = 'horror'
            genre.created_at = date.today()
            test_genre1.updated_at = None
            
            assert (genre == test_genre1)
    
#genre.update()
@patch("application.models.genre.Genre")
def test_should_be_updated_genre(mock_genre):
    mock_genre.query.filter_by(slug=dummy_slug).first.return_value = test_genre1  
    patched_add = MagicMock(spec=sqlalchemy.orm.Session.add)
    patched_commit = MagicMock(spec=sqlalchemy.orm.Session.commit)

    data = {
            'name': 'Western',
            'description': 'western movies',
            'cover': 'https://pictures.com/western-cover.jpg',
    }
    
    with patch('application.db.session.add', new=patched_add):
        with patch('application.db.session.commit', new=patched_commit):
            genre = Genre.get_by_slug(dummy_slug)
            updated_genre = genre.update(data)

            assert (updated_genre.name == data['name'])
            assert (updated_genre.description == data['description'])
            assert (updated_genre.cover == data['cover'])    