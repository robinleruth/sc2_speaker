from typing import List

from app.domain.service.action_connector import ActionConnector
from app.domain.service.action_type import ActionType
from app.domain.model.action import Action
from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.action_model import Action as ActionDb
from app.infrastructure.db.build_order import BuildOrder


class DbFixedActionConnector(ActionConnector):
    def __init__(self, build_order_name=None):
        self.build_order_name = build_order_name

    def get_action_list(self) -> List[Action]:
        lst_to_return = []
        with transaction_context() as session:
            if self.build_order_name is None:
                lst = session.query(ActionDb).all()
            else:
                lst = session.query(BuildOrder).filter_by(name=self.build_order_name).first().actions
            lst = list(filter(lambda x: x.action_type == ActionType.FIXED_ACTION, lst))
            lst_to_return = [Action(i.time, i.name) for i in lst]
        return lst_to_return

    def persist_entry(self, action: Action):
        with transaction_context() as session:
            entry = ActionDb(time=action.time,
                             name=action.name,
                             action_type=ActionType.FIXED_ACTION.value)
            session.add(entry)

    def delete_entry(self, action: Action):
        with transaction_context() as session:
            entry = session.query(ActionDb).filter_by(time=action.time,
                                                      name=action.name).first()
            session.delete(entry)
