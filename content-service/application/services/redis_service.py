from .. import redis

def delete_breadcrumbs(slug: str):
    delete_film_detail(slug)
    delete_films_paginations()
    delete_genre_films_paginations()

def delete_film_detail(slug: str):
    redis.delete('film-detail-' + slug)

def delete_films_paginations():
    for key in redis.keys('films-page-*'):
        redis.delete(key)

def delete_genre_films_paginations():
    for key in redis.keys('genre-films-page-*'):
        redis.delete(key)        

def store_film_detail(slug: str,content: str):
    redis.set('film-detail-' + slug,content)

def get_film_detail(slug: str):
    return redis.get('film-detail-' + slug)

def store_films_page(page: int,content: str):
    redis.set('films-page-' + str(page),content,ex=50)

def get_films_page(page: int):
    return redis.get('films-page-' + str(page))

def store_genre_films_page(page: int,content: str):
    redis.set('genre-films-page-' + str(page),content,ex=50)

def get_genre_films_page(page: int):
    return redis.get('genre-films-page-' + str(page))              