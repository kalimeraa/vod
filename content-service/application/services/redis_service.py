from .. import redis

def delete_breadcrumbs(id: int):
    delete_film_detail(id)
    delete_films_paginations()
    delete_genre_films_paginations()

def delete_film_detail(id: int):
    redis.delete('film-detail-' + str(id))

def delete_films_paginations():
    for key in redis.keys('films-page-*'):
        redis.delete(key)

def delete_genre_films_paginations():
    for key in redis.keys('genre-films-page-*'):
        redis.delete(key)        

def store_film_detail(id: int,content: str):
    redis.set('film-detail-' + str(id),content)

def get_film_detail(id: int):
    return redis.get('film-detail-' + str(id))

def store_films_page(page: int,content: str):
    redis.set('films-page-' + str(page),content,ex=50)

def get_films_page(page: int):
    return redis.get('films-page-' + str(page))

def store_genre_films_page(page: int,content: str):
    redis.set('genre-films-page-' + str(page),content,ex=50)

def get_genre_films_page(page: int):
    return redis.get('genre-films-page-' + str(page))              