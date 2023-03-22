from flask import Flask
from .user.view import user_bp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder="../static")
    app.register_blueprint(user_bp)
    return app