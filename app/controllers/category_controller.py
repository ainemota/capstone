from http import HTTPStatus

from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session

from app.configs.database import db
from flask import request, jsonify

from app.models.category_model import CategoryModel


def post_category():
    data = request.get_json()

    category = CategoryModel(name=data["name"], description=data["description"])

    category.create()

    return jsonify(category), HTTPStatus.CREATED


def get_category():
    session: Session = db.session()

    categories = session.query(CategoryModel).all()

    return jsonify(categories), HTTPStatus.OK


def patch_category(category_id):
    data = request.get_json()
    session: Session = db.session()

    category = session.query(CategoryModel).get(category_id)

    category.update(data)

    return jsonify(category), HTTPStatus.OK


def delete_category(category_id):
    session: Session = db.session()

    category = session.query(CategoryModel).get(category_id)

    category.delete()

    return "", HTTPStatus.NO_CONTENT


def get_by_name_category(name: str):
    session: Session = db.session()

    category = session.query(CategoryModel).filter(CategoryModel.name == name).first()

    return jsonify(category), HTTPStatus.OK
