from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates


@dataclass
class CategoryModel(db.Model):
    id: int
    name: str
    description: str

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    description = Column(String(300), nullable=False)

    def create(self):
        session = db.session()
        session.add(self)
        session.commit()

    def update(self, data):
        for key, value in data.items():
            if not hasattr(self, key):
                continue
            setattr(self, key, value)

        session = db.session()
        session.add(self)
        session.commit()

    def delete(self):
        session = db.session()
        session.delete(self)
        session.commit()

    @validates("name", "description")
    def check_types(self, key, value):
        if key == "name" and type(value) != str:
            raise TypeError

        if key == "description" and type(value) != str:
            raise TypeError

        return value
