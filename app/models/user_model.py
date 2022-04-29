
from werkzeug.security import generate_password_hash, check_password_hash
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class UserModel(db.Model):

    id: str
    name: str
    email: str

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=True)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)