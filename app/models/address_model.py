from flask import current_app
from sqlalchemy import Column, String
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.exceptions.InvalidId import InvalidId

from app.exceptions.InvalidKeys import InvalidKeys

@dataclass
class Address(db.Model):
    id: str
    state: str
    city: str
    street: str
    number: str
    complement: str

    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    state = Column(String(20))
    city = Column(String(20))
    street = Column(String(20))
    number = Column(String(8))
    complement = Column(String(20))

    def create(self):
        session = current_app.db.session
        session.add(self)
        session.commit()
    
    @staticmethod
    def validate_keys(data):
        expecte_keys_set = {"estado", "cidade", "rua", "numero", "complemento"}
        received_keys_set = set(data.keys())

        if received_keys_set.symmetric_difference(expecte_keys_set):
            list_exp_keys = list(expecte_keys_set)
            list_rec_keys = list(received_keys_set)
            raise InvalidKeys(receivedKeys=list_rec_keys, expectedKeys=list_exp_keys)

    @classmethod
    def validate_address_id(cls, address_id):
        address = cls.query.get(address_id)

        if not address:
            raise InvalidId(modelName="address")