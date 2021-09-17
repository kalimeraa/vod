input = {
        "name": "Django Unchained",
        "description": "With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation-owner in Mississippi.",
        "year": 2012,
        "fragman":"https://www.youtube.com/watch?v=django",
        "cover" : "https://imdb.pic/django",
        "genre_id" : 3
}

update_input = {
        "name": "Django Unchained 2",
        "description": "With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation-owner in Mississippi.",
        "year": 2012,
        "fragman":"https://www.youtube.com/watch?v=django",
        "cover" : "https://imdb.pic/django",
        "genre_id" : 3
}

incorrect_input = {
        "name": "Django Unchained",
        "description": "With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation-owner in Mississippi.",
        "year": 2012,
        "fragman":"https://www.youtube.com/watch?v=django",
        "cover" : "https://imdb.pic/django",
}

incorrect_update_input = {
        "name": "Django Unchained 2",
        "description": "With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation-owner in Mississippi.",
        "year": 2012,
        "fragman":"https://www.youtube.com/watch?v=django",
        "cover" : "https://imdb.pic/django",
}

#api/films create film
def test_should_be_created_film(client):
    rv = client.post('/api/films', json=input)
    json = rv.get_json()

    assert (json['status'] == True)
    assert (json['message'] == 'created')    
    assert (rv.status_code == 200)

#api/films create film
def test_should_be_existing_film_error(client):
    rv = client.post('/api/films', json=input)
    rv = client.post('/api/films', json=input)
    json = rv.get_json()

    assert (json['status'] == False)
    assert (json['message'] == 'film is already exist')     
    assert (rv.status_code == 409)

#api/films create film
def test_should_be_genre_required_error_when_create_film(client):
    rv = client.post('/api/films', json=incorrect_input)
    json = rv.get_json()
        
    assert (rv.status_code == 400)
    assert (json == {'genre_id': ['required field']})

#api/films update film
def test_should_be_updated_film(client):
    test_should_be_created_film(client)    
    rv = client.put('/api/films/django-unchained', json=update_input)
        
    assert (rv.status_code == 200)

#api/films update film
def test_should_be_genre_required_error_when_update_film(client):
    test_should_be_created_film(client)    
    rv = client.put('/api/films/django-unchained', json=incorrect_update_input)
    json = rv.get_json()

    assert (rv.status_code == 400)
    assert (json == {'genre_id': ['required field']})

#api/films update film
def test_should_be_film_not_found_error_when_update_film(client):
    rv = client.put('/api/films/dummy-film', json=update_input)
    json = rv.get_json()

    assert (rv.status_code == 404)
    assert (json == {'film': None, 'message': 'film not found', 'status': False})

#api/films delete film
def test_should_be_deleted_film(client):
    test_should_be_created_film(client)
    rv = client.delete('/api/films/django-unchained')
    json = rv.get_json()
    
    assert (rv.status_code == 200)
    assert (json['message'] == 'deleted')
    assert (json['status'] == True)

#api/films delete film
def test_should_be_film_not_found_error_when_delete_film(client):
    rv = client.delete('/api/films/dummy-film')
    json = rv.get_json()

    assert (rv.status_code == 404)
    assert (json == {'film': None, 'message': 'film not found', 'status': False})

#api/films show film
def test_should_be_shown_film(client):
    test_should_be_created_film(client)
    rv = client.get('/api/films/django-unchained')
    json = rv.get_json()

    assert (rv.status_code == 200)
    assert (json['status'] == True)
    assert (json['message'] == 'successful')

#api/films show film
def test_should_be_film_not_found_error_when_show_film(client):
    rv = client.get('/api/films/dummy-film')
    json = rv.get_json()

    assert (rv.status_code == 404)
    assert (json == {'film': None, 'message': 'film not found', 'status': False})

#api/films all
def test_should_show_no_films(client):
    rv = client.get('api/films')
    json = rv.get_json()

    assert (rv.status_code == 404)
    assert (json == {'status':False,'message':'there are no films','films':None})

#api/films all
def test_should_show_two_films(client):
    client.post('/api/films', json=input)
    client.post('/api/films', json=update_input)
    rv = client.get('api/films')
    json = rv.get_json()

    assert (json['status'] == True)
    assert (len(json['films']) == 2)
    assert (json['message'] == 'successful')


