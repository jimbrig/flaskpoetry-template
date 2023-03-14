# -*- coding: utf-8 -*-
"""App Module Flask Extensions"""

import os
from typing import NoReturn

from dynaconf import FlaskDynaconf
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def init_app(app: Flask) -> NoReturn:
    """
    Initialize Flask App with Extensions

    :param:app Flask app object
    :return: NoReturn
    """

    db = SQLAlchemy()
    dbg_toolbar = DebugToolbarExtension()
    migrate = Migrate()

    FlaskDynaconf(
        app,
        instance_relative_config=True,
        SETTINGS_FILE=[
            os.path.join(app.instance_path, ".secrets.settings.toml"),
            os.path.join(app.root_path, "config/settings.toml"),
        ],
    )

    app.config.load_extensions()
    app.config["UPLOAD_FOLDER"] = os.path.join(app.instance_path, "uploads")


# extensions = [db, dynconf, dbg_toolbar, migrate]
