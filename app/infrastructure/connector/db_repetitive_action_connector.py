from typing import List

from app.domain.service.action_connector import ActionConnector
from app.domain.service.action_type import ActionType
from app.domain.model.action import Action
from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.action_model import Action as ActionDb


class DbRepetitiveActionConnector(ActionConnector):
    def get_action_list(self) -> List[Action]:
        lst_to_return = []
        with transaction_context() as session:
            lst = session.query(ActionDb).all()
            lst = list(filter(lambda x: x.action_type == ActionType.REPETITIVE_ACTION, lst))
            lst_to_return = [Action(i.time, i.name) for i in lst]
        return lst_to_return
