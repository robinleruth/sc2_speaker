from typing import List

from app.domain.service.action_connector import ActionConnector
from app.domain.model.action import Action


class TestActionConnector(ActionConnector):
    def get_action_list(self) -> List[Action]:
        a = Action(time=1, name="action1")
        c = Action(time=2, name="action2")
        b = Action(time=1, name="action3")
        lst = [a, b, c]
        return lst
