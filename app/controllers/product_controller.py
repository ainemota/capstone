from http import HTTPStatus
from itertools import product
from flask import request
from app.configs.database import db
from app.exceptions.InvalidId import InvalidId
from app.exceptions.InvalidKeys import InvalidKeys
from app.models.address_model import Address
from app.models.product_model import Product
from flask_jwt_extended import jwt_required


@jwt_required()
def create_product():
    data = request.get_json()

    try:
        Product.validate_keys(data)
    except InvalidKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST

    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
  
    return {"product_created": new_product}, HTTPStatus.CREATED


def products():
    products = Product.query.order_by("id").all()

    return {"products": products}, HTTPStatus.OK


@jwt_required()
def update_product(product_id):
    data = request.get_json()

    try:
        Product.validate_keys(data, update=True)
        product = Product.find_and_validate_id(product_id)
        Product.update(data, product)
    except InvalidKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    return {"updated_product": product}, HTTPStatus.OK


@jwt_required()
def delete_product(product_id):
    try: 
        product = Product.find_and_validate_id(product_id)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    db.session.delete(product)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT


def specific_product(product_id):
    try: 
        product = Product.find_and_validate_id(product_id)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    return {"product": product}, HTTPStatus.OK