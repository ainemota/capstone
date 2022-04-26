from flask import request


def create_product():
    data = request.get_json()

    