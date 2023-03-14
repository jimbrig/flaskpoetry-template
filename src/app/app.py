# -*- coding: utf-8 -*-
"""App Module's app.py"""

import os

from flask import Flask


def create_app():
    """
    Flask Application Factory

    :return: app object
    :rtype: flask.app.Flask
    """

    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    register_extensions(app)
    # register_healthcheck(app)
    # register_blueprints(app)
    # register_errorhandlers(app)
    # register_shellcontext(app)
    # register_commands(app)

    @app.route("/")
    def index():
        return "Hello World!"

    return app


def register_extensions(app):
    """
    Register Flask Extensions

    :param:app Flask app object
    :return: None
    """

    from src.app.exts import extensions

    for ext in extensions:
        ext.init_app(app)

    return None


def register_blueprints(app):
    """
    Register Flask Blueprints

    :param:app Flask app object
    :return: None
    """

    from src.app import auth, main

    blueprints = [auth.bp, main.bp]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return None
