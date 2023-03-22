from flask import Blueprint
user_bp = Blueprint('user', __name__)

@user_bp.route('/hello')
def hello_world():
    return 'hello world'