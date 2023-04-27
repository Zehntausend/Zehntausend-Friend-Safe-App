from flask import Flask

from App.config import load_config
from App.extensions import db, login_manager, cors, jwt_manager
from App.views import views


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(load_config())

    db.init_app(app)
    cors.init_app(app)
    jwt_manager.init_app(app)
    login_manager.init_app(app)

    for view in views:
        app.register_blueprint(view)

    app.app_context().push()
    db.create_all()

    return app
