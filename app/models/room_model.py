from flask import jsonify

from app.configs.database import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import validates
from dataclasses import dataclass


@dataclass
class RoomModel(db.Model):
    id: int
    locator_id: str
    address_id: str
    title: str
    description: str
    status: bool

    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False, unique=True)
    description = Column(String(300), nullable=False)
    status = Column(Boolean, nullable=False)
    locator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    address_id = Column(UUID(as_uuid=True), ForeignKey("addresses.id"), nullable=False)

    def create(self):
        session = db.session()
        session.add(self)
        session.commit()

    def update(self, data):
        for key, value in data.items():
            if not hasattr(self, key):
                continue
            setattr(self, key, value)

        session = db.session()
        session.add(self)
        session.commit()

    def is_the_owner(self, user):
        if str(self.locator_id) != user["id"]:
            return {"error": "you need to be the owner"}

        return True

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



