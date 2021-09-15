from sqlalchemy import event
from slugify import slugify
from ..models.film import Film

@event.listens_for(Film, 'before_insert')
def before_insert_listener(mapper, connection, target):
    target.slug = slugify(target.name)

@event.listens_for(Film, 'before_update')
def before_update_listener(mapper, connection, target):
    target.slug = slugify(target.name)