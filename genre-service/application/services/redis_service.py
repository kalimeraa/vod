from .. import redis

def delete_breadcrumbs(slug: str):
    delete_genre_detail(slug)
    delete_genres_paginations()

def delete_genre_detail(slug: str):
    redis.delete('genre-detail-' + slug)

def delete_genres_paginations():
    for key in redis.keys('genre-page-*'):
        redis.delete(key)

def store_genre_detail(slug: str,content: str):
    redis.set('genre-detail-' + slug,content)

def get_genre_detail(slug: str):
    return redis.get('genre-detail-' + slug)

def store_genres_page(page: int,content: str):
    redis.set('genre-page-' + str(page),content)

def get_genres_page(page: int):
    return redis.get('genre-page-' + str(page))        