from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey


class RoomsCategoriesModel(db.Model):

    __tablename__ = "rooms_categories"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    rooms_id = Column(Integer, ForeignKey("rooms.id"))
