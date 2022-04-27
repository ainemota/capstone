from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from app.exceptions.InvalidKeys import InvalidKeys
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

    @staticmethod
    def validate_keys(data: dict):
        expected_keys_set = {"name", "description", "status", "price", "address_id"}
        received_keys_set = set(data.keys())

        if received_keys_set.symmetric_difference(expected_keys_set):
            list_exp_keys = list(expected_keys_set)
            list_rec_keys = list(received_keys_set)
            raise InvalidKeys(expectedKeys=list_exp_keys, receivedKeys=list_rec_keys)

    @staticmethod
    def validate_address(data: dict):
        if 'address_id' in data.keys():
            Address.validate_address_id(data['address_id'])
            return data
        else:
            address = data.pop('address')
            product_address = Address(**address)
            product_address.create()
            data['address_id'] = product_address.id
            return data