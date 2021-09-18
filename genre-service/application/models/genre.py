# application/models.py
from application import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Genre(db.Model):
    __tablename__ = 'genres'

    id: int
    name: str
    description: str
    cover:str
    slug:str
    created_at: datetime
    updated_at: datetime

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    cover = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),onupdate=db.func.now())

    @staticmethod
    def all():
        return Genre.query.all()

    @staticmethod
    def create(input):
        category = Genre()
        category.name = input['name']
        category.description = input['description']
        category.cover = input['cover']

        db.session.add(category)
        db.session.commit()

        return category

    @staticmethod
    def get_by_id(id: int):
        return Genre.query.filter_by(id=id).first()

    @staticmethod
    def get_by_slug(slug):
        return Genre.query.filter_by(slug=slug).first()

    def delete(self) -> bool:
        try:
            db.session.delete(self)
            db.session.commit()

            return True
        except:
            return False    

    def update(self,input):
        self.name = input['name']
        self.description = input['description']
        self.cover = input['cover']
        
        db.session.add(self)
        db.session.commit()

        return self

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'cover': self.cover,
            'slug': self.slug,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


