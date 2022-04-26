from dataclasses import dataclass
from sqlalchemy import Column, String
from app.configs.database import db
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

    id = Column(UUID, primary_key=True, default=uuid4)
    estado = Column(String(20))
    cidade = Column(String(20))
    rua = Column(String(30))
    numero = Column(String(5))
    complemento = Column(String(50))
