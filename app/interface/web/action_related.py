import time

from flask import Blueprint
from flask import request
from flask import jsonify
from queue import Queue

from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.action_model import Action
from app.infrastructure.log import logger
from app.interface.web.task import async_task
from app.domain.service.main_service import MainService


bp = Blueprint('action_related', __name__)


@bp.route('/api/v1/actions', methods=['DELETE', 'PUT', 'GET', 'POST'])
@bp.route('/api/v1/actions/<int:_id>', methods=['DELETE', 'PUT', 'GET'])
def actions(_id=None):
    if _id:
        if request.method == 'DELETE':
            with transaction_context() as session:
                to_del = session.query(Action).filter_by(id=_id).first()
                logger.info(f'Deleting {to_del}')
                session.delete(to_del)
            return '', 204
        elif request.method == 'GET':
            with transaction_context() as session:
                to_ret = session.query(Action).filter_by(id=_id).first()
                j = to_ret.serialize
            return jsonify(j)
        elif request.method == 'PUT':
            with transaction_context() as session:
                session.expire_on_commit = False
                to_update = session.query(Action).filter_by(id=_id).first()
                logger.info(f'Updating {to_update} with : {request.json}')
                # to_update.__dict__.update(**request.json)
                for k, v in request.json.items():
                    setattr(to_update, k, v)
    else:
        if request.method == 'GET':
            with transaction_context() as session:
                lst = session.query(Action).all()
                lst = [i.serialize for i in lst]
            return jsonify(lst)
        elif request.method == 'POST':
            with transaction_context() as session:
                session.expire_on_commit = False
                new_action = Action(**request.json)
                session.add(new_action)
                session.commit()
                logger.info(f'Creating {new_action}')
                j = new_action.serialize
            return jsonify(j), 201
    return '', 200


@bp.route('/api/v1/run')
@async_task
def run(queue: Queue, queue_from_client: Queue):
    service = MainService()
    service.run()
    while True:
        if not queue_from_client.empty() and queue_from_client.get() == 'STOP':
            break
        lst = service.get_action_from_queue()
        for i in lst:
            queue.put(i)
        time.sleep(1)
    return jsonify({'response': 'ok'})

