# TO DO 
# validar as keys enviadas na requisicao
# caso o endereco nao seja enviado usar o endereco do usuario

from http import HTTPStatus
from flask import request
from app.configs.database import db
from app.exceptions.InvalidIa import InvalidId
from app.exceptions.InvalidKeys import InvalidKeys
from app.models.address_model import Address
from app.models.product_model import Product


def create_product():
    data = request.get_json()

    try:
        data = Product.validate_address(data)
        Product.validate_keys(data)
    except InvalidKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND

    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
  
    return {"product_created": new_product}, HTTPStatus.CREATED