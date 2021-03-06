import uuid
from logging import addLevelName
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import validates, relationship
from app.exceptions.AlreadyExists import AlreadyExists
from app.exceptions.InvalidType import InvalidType
from app.models.address_model import Address


@dataclass
class UserModel(db.Model):
    id: str
    name: str
    email: str
    address_id: Address

    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=True)
    address_id = db.Column(
        UUID(as_uuid=True), ForeignKey("addresses.id"), nullable=False
    )

    rentals = relationship("Rental", back_populates="lessee")

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    @validates("name", "email", "password", "address_id", "address")
    def check_types(self, key, value):
        if key == "name" and type(value) != str:
            raise InvalidType(key, "str")

        if key == "email" and type(value) != str:
            raise InvalidType(key, "str")

        if key == "password" and type(value) != str:
            raise InvalidType(key, "str")

        if key == "address":
            if type(value) != dict and type(value) != str:
                raise InvalidType(key, "str")

        return value

    @classmethod
    def validate_email(cls, data):
        user_email = data["email"]
        email_exists = cls.query.filter_by(email=user_email).first()

        if email_exists:
            raise AlreadyExists("email")

    @staticmethod
    def create_user_address(data):
        address = data.pop("address")

        Address.validate_CEP(address)
        new_address = Address(**address)
        new_address.create()

        data["address_id"] = new_address.id

        return data
