from flask import current_app
from sqlalchemy import Column, String
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

@dataclass
class Address(db.Model):
    id: str
    estado: str
    cidade: str
    rua: str
    numero: str
    complemento: str

    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    estado = Column(String(20))
    cidade = Column(String(20))
    rua = Column(String(20))
    numero = Column(String(8))
    complemento = Column(String(20))

    def create(self):
        session = current_app.db.session
        session.add(self)
        session.commit()