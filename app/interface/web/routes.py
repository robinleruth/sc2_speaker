from flask import Blueprint


bp = Blueprint(__name__, 'main')


@bp.route('/')
def index():
    return 'Hello World'
