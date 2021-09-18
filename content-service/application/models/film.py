# application/models.py
from application import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Film(db.Model):
    __tablename__ = 'films'

    id: int
    name: str
    description: str
    fragman: str
    cover:str
    year:int
    genre_id:int
    slug:str
    created_at: datetime
    updated_at: datetime

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    fragman = db.Column(db.String(255), nullable=False)
    cover = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre_id = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),onupdate=db.func.now())

    @staticmethod
    def all():
        return Film.query.all()

    @staticmethod
    def create(content):
        film = Film()
        film.name = content['name']
        film.description = content['description']
        film.year = content['year']
        film.cover = content['cover']
        film.fragman = content['fragman']
        film.genre_id = content['genre_id']

        db.session.add(film)
        db.session.commit()

        return film

    @staticmethod
    def get_by_slug(slug):
        return Film.query.filter_by(slug=slug).first()

    @staticmethod
    def get_by_id(id):
        return Film.query.filter_by(id=id).first()    

    def delete(self) -> bool:
        try:
            db.session.delete(self)
            db.session.commit()

            return True
        except:
            return False    

    def update(self,content):
        self.name = content['name']
        self.cover = content['cover']
        self.fragman = content['fragman']
        self.description = content['description']
        self.year = content['year']
        self.genre_id = content['genre_id']

        db.session.add(self)
        db.session.commit()

        return self

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'fragman': self.fragman,
            'cover': self.cover,
            'year': self.year,
            'genre_id': self.genre_id,
            'slug': self.slug,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


