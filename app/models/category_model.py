from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String


@dataclass
class CategoryModel(db.Model):
    category_id: int
    name: str
    description: str

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    description = Column(String(300), nullable=False)
