from app.configs.database import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import validates
from dataclasses import dataclass


@dataclass
class RoomModel(db.Model):
    title: str
    description: str
    status: bool

    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False, unique=True)
    description = Column(String(300), nullable=False)
    status = Column(Boolean, nullable=False)
    locator = Column(Integer, ForeignKey("users.id"), nullable=True)
    address = Column(UUID(as_uuid=True), ForeignKey("addresses.id"), nullable=False)

    @validates("title", "description", "status", "products")
    def check_types(self, key, value):
        if key == "title" and type(value) != str:
            raise TypeError

        if key == "description" and type(value) != str:
            raise TypeError

        if key == "status" and type(value) != bool:
            raise TypeError

        if key == "products" and type(value) != bool:
            raise TypeError

        return value
