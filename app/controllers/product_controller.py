# TO DO 
# validar as keys enviadas na requisicao
# caso o endereco nao seja enviado usar o endereco do usuario

from http import HTTPStatus
from flask import request
from app.configs.database import db
from app.models.address_model import Address
from app.models.product_model import Product


def create_product():
    data = request.get_json()

    if 'address_id' in data.keys():
        new_product = Product(**data)
    else:
        address = data.pop('address')
        product_address = Address(**address)
        product_address.create()
        data['address_id'] = product_address.id
        new_product = Product(**data)

    db.session.add(new_product)
    db.session.commit()
  
    return {"product_created": new_product}, HTTPStatus.CREATED