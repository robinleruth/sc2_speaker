from flask import Blueprint
from flask import request
from flask import jsonify

from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.action_model import Action


bp = Blueprint('action_related', __name__)


@bp.route('/api/v1/actions', methods=['DELETE', 'PUT', 'GET', 'POST'])
@bp.route('/api/v1/actions/<int:id>', methods=['DELETE', 'PUT', 'GET'])
def actions(_id=None):
    if _id:
        if reqeust.method == 'DELETE':
            with transaction_context() as session:
                to_del = session.query(Action).filter_by(id=_id).first()
                session.delete(to_del)
        elif request.method == 'GET':
            with transaction_context() as session:
                to_ret = session.query(Action).filter_by(id=_id).first()
                j = to_ret.serialize
            return jsonify(j)
        elif request.method == 'PUT':
            with transaction_context() as session:
                to_update = session.query(Action).filter_by(id=_id).first()
                to_update.__dict__.update(**request.json)
    else:
        if request.method == 'GET':
            with transaction_context() as session:
                lst = session.query(Action).all()
                lst = [i.serialize for i in lst]
            return jsonify(lst)
        elif request.method == 'POST':
            with transaction_context() as session:
                new_action = Action(**request.json)
                session.add(new_action)
                session.commit()
                j = new_action.serialize
            return jsonify(j)
    return '', 200
