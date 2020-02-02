from flask import Flask
from flask_nav import Nav
from flask_bootstrap import Bootstrap

from app.infrastructure.config import app_config

nav = Nav()
bootstrap = Bootstrap()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(app_config)
    nav.init_app(app)
    bootstrap.init_app(app)

    from app.interface.web.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
