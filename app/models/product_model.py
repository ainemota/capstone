from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from app.models.address_model import Address


@dataclass
class Product(db.Model):
    id: int
    name: str
    description: str
    status: str
    price: float
    address: Address
    # locator_id: str
    # room: Room

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(Text)
    status = Column(String(15))
    price = Column(Float)
    address_id = Column(UUID(as_uuid=True), ForeignKey("addresses.id"), nullable=True)
    address = relationship("Address", backref="products")