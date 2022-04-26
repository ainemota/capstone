from flask import Blueprint


def init_app(app):
    # registrar todas as blueprints criadas importando-as
    app.register_blueprint()