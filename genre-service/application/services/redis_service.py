from .. import redis

def delete_breadcrumbs(id: int):
    delete_genre_detail(id)
    delete_genres_paginations()

def delete_genre_detail(id: int):
    redis.delete('genre-detail-' + str(id))

def delete_genres_paginations():
    for key in redis.keys('genre-page-*'):
        redis.delete(key)

def store_genre_detail(id: int,content: str):
    redis.set('genre-detail-' + str(id),content,ex=50)

def get_genre_detail(id: int):
    return redis.get('genre-detail-' + str(id))

def store_genres_page(page: int,content: str):
    redis.set('genre-page-' + str(page),content,ex=50)

def get_genres_page(page: int):
    return redis.get('genre-page-' + str(page))        