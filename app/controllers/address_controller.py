from http import HTTPStatus
from flask import current_app, request
from app.exceptions.InvalidKeys import InvalidKeys
from app.exceptions.InvalidId import InvalidId
from app.models.address_model import Address


def create_address():
    data = request.get_json()

    try:
        Address.validate_keys(data)
    except InvalidKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST

    new_address = Address(**data)
    new_address.create()

    return {"address_created": new_address}, HTTPStatus.CREATED


def addresses():
    addresses = Address.query.order_by("id").all()

    return {"addresses": addresses}, HTTPStatus.OK


def update_address(address_id):
    data = request.get_json()

    try:
        Address.validate_keys(data, update=True)
        address = Address.find_and_validate_id(address_id)
        Address.update(data, address)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    except InvalidKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST

    return {"updated_address": address}, HTTPStatus.OK


def delete_address(address_id):
    try: 
        address = Address.find_and_validate_id(address_id)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    current_app.db.session.delete(address)
    current_app.db.session.commit()

    return {}, HTTPStatus.NO_CONTENT


def specific_address(address_id):
    try: 
        address = Address.find_and_validate_id(address_id)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    return {"address": address}, HTTPStatus.OK
