from dataclasses  import dataclass
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, ForeignKey, Integer, DateTime
from app.configs.database import db
from sqlalchemy.orm import relationship


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
    lessee_id = Column(UUID(ass_uuid=True), ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    lease_price_unit = Column(Float, nullable=False)

    lessee = relationship("UserModel", backref="rentals")
    room = relationship("RoomModel", backref="rentals")
    product = relationship("Product", backref="rentals")
