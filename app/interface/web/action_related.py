import time
import datetime as dt

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import Response
from queue import Queue

from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.action_model import Action
from app.infrastructure.db.build_order import BuildOrder
from app.infrastructure.log import logger
from app.infrastructure.connector.db_fixed_action_connector import DbFixedActionConnector
from app.interface.web.task import async_task
from app.domain.service.main_service import MainService


bp = Blueprint('action_related', __name__)


@bp.route('/api/v1/get_all_build_orders_name')
def get_all_build_orders_name():
    with transaction_context() as session:
        lst = session.query(BuildOrder).all()
        lst = [i.name for i in lst]
    return jsonify(lst)


@bp.route('/api/v1/create_new_build_order', methods=['POST'])
def create_new_build_order():
    name = request.form['name']
    with transaction_context() as session:
        session.expire_on_commit = False
        lst = session.query(BuildOrder).filter_by(name=name).all()
        if len(lst) == 0:
            entry = BuildOrder(name=name)
            session.add(entry)
        else:
            entry = lst[0]
    j = entry.serialize
    return jsonify(j)


@bp.route('/api/v1/actions/<build_order>', methods=['DELETE', 'PUT', 'GET', 'POST'])
@bp.route('/api/v1/actions/<build_order>/<int:_id>', methods=['DELETE', 'PUT', 'GET'])
def actions(build_order=None, _id=None):
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
                session.add(to_update)
    else:
        if request.method == 'GET':
            with transaction_context() as session:
                lst = session.query(BuildOrder).filter_by(name=build_order).first().actions
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


@bp.route('/stream_run')
def stream_run():
    build_order_name = request.args['name']
    fixed_action_connector = DbFixedActionConnector(build_order_name)
    def gen():
        service = MainService(fixed_action_connector)
        service.run()
        while True:
            lst = service.get_action_from_queue()
            for i in lst:
                yield str(dt.timedelta(seconds=int(i.time))) + ' : ' + i.name + '\n'
            time.sleep(1)
    return Response(gen())
