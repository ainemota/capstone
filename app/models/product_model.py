from sqlalchemy import Column, Float, Integer, String
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Product(db.Model):
    id: int
    name:str
    status: str
    description: str
    prince: float
    # room: Room
    # locator: User

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String(12))
    description = Column(String(100))
    prince = Column(Float)