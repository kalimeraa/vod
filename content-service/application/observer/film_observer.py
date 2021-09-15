from sqlalchemy import event
from slugify import slugify
from ..models.film import Film
from .. import redis
from ..services.redis_service import delete_breadcrumbs

@event.listens_for(Film, 'before_insert')
def before_insert_listener(mapper, connection, target):
    target.slug = slugify(target.name)

@event.listens_for(Film, 'before_update')
def before_update_listener(mapper, connection, target):
    target.slug = slugify(target.name)

@event.listens_for(Film, 'after_insert')
def receive_after_insert(mapper, connection, target):
    delete_breadcrumbs(target.slug)

@event.listens_for(Film, 'after_update')
def receive_after_update(mapper, connection, target):
    delete_breadcrumbs(target.slug)

@event.listens_for(Film, 'after_delete')
def receive_after_delete(mapper, connection, target):
    delete_breadcrumbs(target.slug)