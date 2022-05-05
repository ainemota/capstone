from http import HTTPStatus
from flask import request
from app.exceptions.InvalidId import InvalidId
from app.configs.database import db
from app.models.rentals_model import Rental


def create_rental():
    data = request.get_json()

    new_rental = Rental(**data)

    return {"rental_created": new_rental}, HTTPStatus.CREATED

def user_rentals(user_id):
    data = request.get_json()

    if data:
        date = data['start_date']
        rentals = Rental.query.filter_by(start_date=date, lessee_id=user_id).all()
    else:
        rentals = Rental.query.filter_by(lessee_id=user_id).all()

    return {"data": rentals}, HTTPStatus.OK


def delete(rental_id):
    try: 
        product = Rental.find_and_validate(rental_id)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    db.session.delete(product)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT