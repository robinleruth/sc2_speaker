from typing import List

from app.domain.service.action_connector import ActionConnector
from app.domain.model.action import Action


class TestRepetitiveActionConnector(ActionConnector):
    def get_action_list(self) -> List[Action]:
        a = Action(time=0, name="creep")
        c = Action(time=0, name="inject")
        lst = [a, c]
        return lst
