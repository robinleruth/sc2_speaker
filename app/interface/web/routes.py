from flask import Blueprint
from flask import render_template
from flask_nav.elements import Navbar
from flask_nav.elements import View

from . import nav


bp = Blueprint('main', __name__)


@nav.navigation()
def top():
    return Navbar('SC2 Speaker',
                  View('Index', 'main.index'),
                  View('Admin', 'admin.index'),
                  View('Logs', 'stream_log.stream_log'),
                  )


@bp.route('/')
def index():
    return render_template('index.html')
