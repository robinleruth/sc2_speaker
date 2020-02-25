from flask import Flask
from flask_nav import Nav
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.infrastructure.config import app_config
from app.infrastructure.db import Session
from app.infrastructure.db.log import Log
from app.infrastructure.db.param_model import Param
from app.infrastructure.db.action_model import Action
from app.infrastructure.log import logger

nav = Nav()
bootstrap = Bootstrap()
admin = Admin()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(app_config)
    nav.init_app(app)
    bootstrap.init_app(app)
    admin.init_app(app)
    admin.add_view(ModelView(Action, Session))
    admin.add_view(ModelView(Param, Session))
    admin.add_view(ModelView(Log, Session))

    from app.interface.web.routes import bp as main_bp
    app.register_blueprint(main_bp)
    from app.interface.web.stream_logs import bp as stream_bp
    app.register_blueprint(stream_bp)
    from app.interface.web.action_related import bp as action_bp
    app.register_blueprint(action_bp)

    logger.info('start up')
    return app
