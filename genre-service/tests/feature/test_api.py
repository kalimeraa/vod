input = {
    "name": "Horror",
    "description": "horror movies",
    "cover" : "https://imdb.pic/horror.jpg",
        
}

update_input = {
    "name": "Fiction",
    "description": "fiction movies",
    "cover" : "https://imdb.pic/fiction.jpg",
}

incorrect_input = {
    "name": "Fiction",
    "cover" : "https://imdb.pic/fiction.jpg",
}

incorrect_update_input = {
    "description": "fiction movies",
    "cover" : "https://imdb.pic/fiction.jpg",
}

#api/genres create genre
def test_should_be_created_genre(client):
    rv = client.post('/api/genres', json=input)
    json = rv.get_json()

    assert (json['status'] == True)
    assert (json['message'] == 'created')
    assert (rv.status_code == 200)

#api/genres create genre
def test_should_be_existing_genre_error(client):
    rv = client.post('/api/genres', json=input)
    rv = client.post('/api/genres', json=input)
    json = rv.get_json()

    assert (json['status'] == False)
    assert (json['message'] == 'genre is already exist')     
    assert (rv.status_code == 409)

#api/genres create genre
def test_should_be_description_required_error_when_create_genre(client):
    rv = client.post('/api/genres', json=incorrect_input)
    json = rv.get_json()
        
    assert (rv.status_code == 400)
    assert (json == {'description': ['required field']})

#api/genres update genre
def test_should_be_updated_genre(client):
    test_should_be_created_genre(client)
    rv = client.put('/api/genres/horror', json=update_input)
        
    assert (rv.status_code == 200)

#api/genres update genre
def test_should_be_name_required_error_when_update_genre(client):
    test_should_be_created_genre(client)    
    rv = client.put('/api/genres/horror', json=incorrect_update_input)
    json = rv.get_json()

    assert (rv.status_code == 400)
    assert (json == {'name': ['required field']})

#api/genres update genre
def test_should_be_genre_not_found_error_when_update_genre(client):
    rv = client.put('/api/genres/dummy-genre', json=update_input)
    json = rv.get_json()

    assert (rv.status_code == 404)
    assert (json == {'genre': None, 'message': 'genre not found', 'status': False})

#api/genres delete genre
def test_should_be_deleted_genre(client):
    test_should_be_created_genre(client)
    rv = client.delete('/api/genres/horror')
    json = rv.get_json()
    
    assert (rv.status_code == 200)
    assert (json['message'] == 'deleted')
    assert (json['status'] == True)

#api/genres delete genre
def test_should_be_genre_not_found_error_when_delete_genre(client):
    rv = client.delete('/api/genres/dummy-genre')
    json = rv.get_json()

    assert (rv.status_code == 404)
    assert (json == {'genre': None, 'message': 'genre not found', 'status': False})

#api/genres show genre
def test_should_be_shown_genre(client):
    test_should_be_created_genre(client)
    rv = client.get('/api/genres/horror')
    json = rv.get_json()

    assert (rv.status_code == 200)
    assert (json['status'] == True)
    assert (json['message'] == 'successful')

#api/genres show genre
def test_should_be_genre_not_found_error_when_show_genre(client):
    rv = client.get('/api/genres/dummy-genre')
    json = rv.get_json()

    assert (rv.status_code == 404)
    assert (json == {'genre': None, 'message': 'genre not found', 'status': False})

#api/genres all
def test_should_show_no_genres(client):
    rv = client.get('api/genres')
    json = rv.get_json()

    assert (rv.status_code == 404)
    assert (json == {'status':False,'message':'there are no genres','genres':None})

#api/genres all
def test_should_show_two_genres(client):
    client.post('/api/genres', json=input)
    client.post('/api/genres', json=update_input)
    rv = client.get('api/genres')
    json = rv.get_json()

    assert (json['status'] == True)
    assert (len(json['genres']) == 2)
    assert (json['message'] == 'successful')

