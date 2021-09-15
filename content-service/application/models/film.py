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
    category_id:int
    slug:str
    created_at: datetime
    updated_at: datetime

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    fragman = db.Column(db.String(255), nullable=False)
    cover = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),onupdate=db.func.now())

    @staticmethod
    def all():
        return Film.query.all()

    @staticmethod
    def getBySlug(slug):
        return Film.query.filter_by(slug=slug).first()

    @staticmethod
    def deleteBySlug(slug):
        return True

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'fragman': self.fragman,
            'cover': self.cover,
            'year': self.year,
            'category_id': self.category_id,
            'slug': self.slug,
        }


