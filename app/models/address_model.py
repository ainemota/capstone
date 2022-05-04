from flask import current_app
from sqlalchemy import Column, String
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.exceptions.AlreadyExists import AlreadyExists
from app.exceptions.InvalidId import InvalidId
from sqlalchemy.orm import validates
from app.exceptions.InvalidKeys import InvalidKeys


@dataclass
class Address(db.Model):
    id: str
    CEP: str
    number: str
    complement: str

    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    CEP = Column(String, nullable=False)
    number = Column(String(8))
    complement = Column(String(20))

    @validates("CEP", "number", "complement")
    def check_types(self, key, value):
        if key == "CEP" and type(value) != str:
            raise TypeError

        if key == "number" and type(value) != str:
            raise TypeError

        if key == "complement" and type(value) != str:
            raise TypeError

        return value

    def create(self):
        session = current_app.db.session
        session.add(self)
        session.commit()
    
    @staticmethod
    def validate_CEP(data):
        valid_address = Address.query.filter_by(CEP=data['CEP']).first()

        if valid_address:
            raise AlreadyExists("CEP")

    @staticmethod
    def validate_keys(data, update=False):
        expecte_keys_set = {"CEP", "number", "complement"}
        received_keys_set = set(data.keys())

        if update:
            if not received_keys_set.issubset(expecte_keys_set):
                list_exp_keys = list(expecte_keys_set)
                list_rec_keys = list(received_keys_set)
                raise InvalidKeys(receivedKeys=list_rec_keys, expectedKeys=list_exp_keys)
        else:
            if received_keys_set.symmetric_difference(expecte_keys_set):
                list_exp_keys = list(expecte_keys_set)
                list_rec_keys = list(received_keys_set)
                raise InvalidKeys(receivedKeys=list_rec_keys, expectedKeys=list_exp_keys)

    @classmethod
    def find_and_validate_id(cls, address_id):
        address = cls.query.get(address_id)

        if not address:
            raise InvalidId(modelName="address")
        else:
            return address

    @staticmethod
    def update(data, address):
        for key, value in data.items():
            setattr(address, key, value)
        
        db.session.add(address)
        db.session.commit()

    @staticmethod
    def create_sql_rule():
        query = """
                CREATE OR REPLACE FUNCTION haversine(
                    latitude1 numeric(10,6),
                    longitude1 numeric(10,6),
                    latitude2 numeric(10,6),
                    longitude2 numeric(10,6))
                RETURNS double precision AS
                $BODY$
                    SELECT 6371 * acos(
                        cos( radians(latitude1) ) * cos( radians( latitude2 ) ) * cos( radians( longitude1 )
                         - 
                        radians(longitude2) )
                         + 
                        sin( radians(latitude1) ) * sin( radians( latitude2 ) ) 
                        ) AS distance
                $BODY$
                LANGUAGE sql;
        """
        db.session.execute(query)

