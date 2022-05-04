from dataclasses  import dataclass

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, ForeignKey, Integer, DateTime
from app.configs.database import db
from sqlalchemy.orm import relationship, validates


@dataclass
class Rental(db.Model):
    lessee_id: str
    room_id: int
    product_id: int
    rental_id: int
    start_date: str
    end_date: str
    lease_price_unit: float

    __tablename__ = "rentals"

    rental_id = Column(Integer, primary_key=True) 
    lessee_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    lease_price_unit = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    lessee = relationship("UserModel", backref="rentals")
    room = relationship("RoomModel", backref="rentals")
    product = relationship("Product", backref="rentals")

    @validates("lessee_id", "product_id", "room_id", "start_date", "end_date", "lease_price_unit", "quantity")
    def check_types(self, key, value):
        if key == "lessee_id" and type(value) != str:
            raise TypeError

        if key == "room_id" and type(value) != int:
            raise TypeError

        if key == "product_id" and type(value) != int:
            raise TypeError

        if key == "start_date" and type(value) != str:
            raise TypeError

        if key == "end_date" and type(value) != str:
            raise TypeError

        if key == "lease_price_unit" and type(value) != float:
            raise TypeError

        if key == "quantity" and type(value) != int:
            raise TypeError

        return value