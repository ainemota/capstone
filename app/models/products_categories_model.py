from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey


class ProductCategorieModel(db.Model):

    __tablename__ = "products_categories"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    def create(self):
        session = db.session()
        session.add(self)
        session.commit()