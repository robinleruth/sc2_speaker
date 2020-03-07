import time
import uuid

from queue import Queue
from functools import wraps
from threading import Thread

from flask import url_for
from flask import Blueprint
from flask import jsonify
from flask import request
from flask import abort
from flask import current_app
from werkzeug.exceptions import HTTPException


bp = Blueprint('tasks', __name__)


tasks = {}


def timestamp():
    return int(time.time())


@bp.before_app_first_request
def before_first_task():
    def clean_old_task():
        global tasks
        while True:
            five_min_ago = timestamp() - 5 * 60
            tasks = {_id: task for _id, task in tasks.items() if 't' not in task
                     or task['t'] > five_min_ago}
            time.sleep(60)
    Thread(target=clean_old_task).start()


def async_task(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        def task(app, environ, _id, queue, queue_from_client):
            with app.request_context(environ):
                try:
                    tasks[_id]['rv'] = f(queue, queue_from_client, *args, **kwargs)
                except HTTPException as e:
                    tasks[_id]['rv'] = jsonify({'response': str(e)}), 404
                except Exception as e:
                    tasks[_id]['rv'] = jsonify({'response': str(e)}), 500
                finally:
                    tasks[_id]['t'] = timestamp()

        _id = uuid.uuid4().hex
        queue = Queue()
        queue_from_client = Queue()
        tasks[_id] = {'tasks': Thread(target=task,
                                      args=(current_app._get_current_object(),
                                            request.environ, _id, queue, queue_from_client))}
        tasks[_id]['queue'] = queue
        tasks[_id]['queue_from_client'] = queue_from_client
        tasks[_id]['tasks'].start()
        return jsonify({'response': 'launching'}), 202, {'Location':
                                                         url_for('tasks.get_status',
                                                                 _id=_id)}
    return wrapped

@bp.route('/status/<_id>', methods=['GET'])
def get_status(_id):
    task = tasks.get(_id)
    if task is None:
        abort(404)
    if 'rv' not in task:
        queue = task['queue']
        if queue.empty():
            response = ''
        else:
            response = task['queue'].get()
        return jsonify({'response': response}), 202, {'Location': url_for('tasks.get_status', _id=_id), 'Kill': url_for('tasks.kill_task', _id=_id)}
    return task['rv']


@bp.route('/kill/<_id>', methods=['GET'])
def kill_task(_id):
    task = tasks.get(_id)
    if task is None:
        abort(404)
    queue = task['queue_from_client']
    queue.put('STOP')
    return jsonify({'response': 'done'})
