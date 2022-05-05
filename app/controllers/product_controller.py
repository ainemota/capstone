from http import HTTPStatus
from itertools import product
from flask import request
from app.configs.database import db
from app.exceptions.InvalidId import InvalidId
from app.exceptions.InvalidKeys import InvalidKeys
from app.models.address_model import Address
from app.models.product_model import Product
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create():
    data = request.get_json()
    
    user = get_jwt_identity()
    data['locator_id'] = user['id']

    try:
        Product.validate_keys(data)
    except InvalidKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST

    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    
    Product.validate_create_categories()
    
    return {"product_created": new_product}, HTTPStatus.CREATED


@jwt_required()
def products():
    products = Product.query.order_by("id").all()

    return {"products": products}, HTTPStatus.OK


@jwt_required()
def update(product_id):
    data = request.get_json()
    user = get_jwt_identity()

    try:
        Product.validate_keys(data, update=True)
        product: Product= Product.find_and_validate_id(product_id)
        product.validate_user(user['id'])
        Product.update(data, product)
    except InvalidKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    return {"updated_product": product}, HTTPStatus.OK


@jwt_required()
def delete(product_id):
    try: 
        product = Product.find_and_validate_id(product_id)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    db.session.delete(product)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT


def specific(product_id):
    try: 
        product = Product.find_and_validate_id(product_id)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    return {"product": product}, HTTPStatus.OK


@jwt_required
def available():
    available_products = Product.query.filter_by(available=True).all()

    return {"available_products": available_products}, HTTPStatus.OK