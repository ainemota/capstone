from flask import current_app
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text, Boolean
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref, validates
from app.exceptions.InvalidId import InvalidId
from app.exceptions.InvalidKeys import InvalidKeys
from app.exceptions.InvalidType import InvalidType
from app.exceptions.InvalidUser import InvalidUser
from app.models.address_model import Address
from app.models.category_model import CategoryModel
from app.models.room_model import RoomModel
from app.models.products_categories_model import ProductCategorieModel


@dataclass
class Product(db.Model):
    id: int
    name: str
    description: str
    available: bool
    price: float
    locator_id: str
    room_id: int

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(Text)
    available = Column(Boolean, nullable=False)
    price = Column(Float)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=True)
    locator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    categories = relationship(
        "CategoryModel", secondary="products_categories", backref="products"
    )

    def validate_user(self, user_id):
        if self.locator_id != user_id:
            raise InvalidUser

    @validates("name", "description", "available", "price", "room_id")
    def check_types(self, key, value):
        if key == "name" and type(value) != str:
            raise InvalidType(key, "str")

        if key == "description" and type(value) != str:
            raise InvalidType(key, "str")

        if key == "available" and type(value) != bool:
            raise InvalidType(key, "str")

        if key == "price" and type(value) != float:
            raise InvalidType(key, "float")

        if key == "room_id" and type(value) != int:
            raise InvalidType(key, "int")

        if key == "locator_id" and type(value) != str:
            raise InvalidType(key, "str")

        return value

    @staticmethod
    def validate_keys(data: dict, update=False):
        expected_keys_set = {"name", "description", "available", "price", "locator_id"}
        received_keys_set = set(data.keys())

        if update:
            if not received_keys_set.issubset(expected_keys_set):
                list_exp_keys = list(expected_keys_set)
                list_rec_keys = list(received_keys_set)
                raise InvalidKeys(
                    expectedKeys=list_exp_keys, receivedKeys=list_rec_keys
                )
        else:
            if received_keys_set.symmetric_difference(expected_keys_set):
                list_exp_keys = list(expected_keys_set)
                list_rec_keys = list(received_keys_set)
                raise InvalidKeys(
                    expectedKeys=list_exp_keys, receivedKeys=list_rec_keys
                )

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

    @staticmethod
    def validate_create_categories(product_id, categories):
        for category in categories:
            category_product = CategoryModel.query.filter_by(name=category).first()
            
            if not category_product:
                category_product = CategoryModel(name=category['name'], description="")
                category_product.create()
            
            relation = ProductCategorieModel(product_id=product_id, category_id=category_product.id)