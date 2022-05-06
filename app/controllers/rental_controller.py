from http import HTTPStatus
from flask import request
from app.exceptions.InvalidId import InvalidId
from app.configs.database import db
from app.models.rentals_model import Rental
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create_rental():
    data = request.get_json()
    user = get_jwt_identity()
    data['lessee_id'] = user['id']

    new_rental = Rental(**data)

    db.session.add(new_rental)
    db.session.commit()
    return {"rental_created": new_rental}, HTTPStatus.CREATED


@jwt_required()
def user_rentals():
    # data = request.get_json()
    user = get_jwt_identity()

    # if data:
    #     date = data['start_date']
    #     rentals = Rental.query.filter_by(start_date=date, lessee_id=user['id']).all()
    # else:
    rentals = Rental.query.filter_by(lessee_id=user['id']).all()

    return {"data": rentals}, HTTPStatus.OK


@jwt_required()
def delete(rental_id):
    try: 
        product = Rental.find_and_validate(rental_id)
    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND
    
    db.session.delete(product)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT