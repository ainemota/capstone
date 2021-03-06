from dataclasses  import dataclass

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, ForeignKey, Integer, DateTime
from app.configs.database import db
from sqlalchemy.orm import relationship, validates

from app.exceptions.InvalidType import InvalidType
from app.exceptions.InvalidId import InvalidId


@dataclass
class Rental(db.Model):
    rental_id: int
    lessee_id: str
    room_id: int
    product_id: int
    start_date: str
    end_date: str
    lease_price_unit: float
    quantity: int

    __tablename__ = "rentals"

    rental_id = Column(Integer, primary_key=True) 
    lessee_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    lease_price_unit = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    lessee = relationship("UserModel", back_populates="rentals")
    room = relationship("RoomModel", backref="rentals")
    product = relationship("Product", backref="rentals")

    @validates("lessee_id", "product_id", "room_id", "start_date", "end_date", "lease_price_unit", "quantity")
    def check_types(self, key, value):
        if key == "lessee_id" and type(value) != str:
            raise InvalidType(key, "str")

        if key == "room_id" and type(value) != int:
            raise InvalidType(key, "int")

        if key == "product_id" and type(value) != int:
            raise InvalidType(key, "int")

        if key == "start_date" and type(value) != str:
            raise InvalidType(key, "str")

        if key == "end_date" and type(value) != str:
            raise InvalidType(key, "str")

        if key == "lease_price_unit" and type(value) != float:
            raise InvalidType(key, "float")

        if key == "quantity" and type(value) != int:
            raise InvalidType(key, "int")

        return value
    
    @classmethod
    def find_and_validate(cls,rental_id):
        rental = cls.query.get(rental_id)

        if not rental:
            raise InvalidId(modelName="Rental")
        else:
            return rental
