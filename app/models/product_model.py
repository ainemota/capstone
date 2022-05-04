from flask import current_app
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from app.exceptions.InvalidId import InvalidId
from app.exceptions.InvalidKeys import InvalidKeys
from app.models.address_model import Address
from app.models.room_model import RoomModel


@dataclass
class Product(db.Model):
    id: int
    name: str
    description: str
    status: str
    price: float
    locator_id: str
    room_id: int

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(Text)
    status = Column(String(15))
    price = Column(Float)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=True)
    locator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    @staticmethod
    def validate_keys(data: dict, update=False):
        expected_keys_set = {"name", "description", "status", "price", "address_id"}
        received_keys_set = set(data.keys())

        if update:
            if not received_keys_set.issubset(expected_keys_set):
                list_exp_keys = list(expected_keys_set)
                list_rec_keys = list(received_keys_set)
                raise InvalidKeys(expectedKeys=list_exp_keys, receivedKeys=list_rec_keys)
        else:
            if received_keys_set.symmetric_difference(expected_keys_set):
                list_exp_keys = list(expected_keys_set)
                list_rec_keys = list(received_keys_set)
                raise InvalidKeys(expectedKeys=list_exp_keys, receivedKeys=list_rec_keys)

    @classmethod
    def find_and_validate_id(cls, product_id):
        product = cls.query.get(product_id)

        if not product:
            raise InvalidId(modelName="Product")
        else:
            return product

    @staticmethod
    def update(data, product):
        for key, value in data.items():
                setattr(product, key, value)
        
        db.session.add(product)
        db.session.commit()
