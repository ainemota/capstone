from uuid import UUID
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from app.configs.database import db
from dataclasses import dataclass
from app.models.address_model import Address
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class Product(db.Model):
    id: int
    name:str
    status: str
    description: str
    prince: float
    address: Address
    # room: Room
    # locator: User

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String(12))
    description = Column(String(100))
    prince = Column(Float)
    address_id = Column(UUID, ForeignKey("addresses.id"), nullable=True)
    address = relationship("Address", backref=backref("product", uselist=False))