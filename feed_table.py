import pandas as pd

from app.domain.model.action import Action
from app.domain.service.main_service import MainService
from app.domain.service.action_type import ActionType


if __name__ == '__main__':
    lst_fixed = [Action(time=1, name="test"), Action(time=2, name="test"),
                Action(time=3, name="test"), Action(time=4, name="test")]

    lst_rep = [Action(time=0, name="test"), Action(time=0, name="test"),
            Action(time=0, name="test")]

    service = MainService()

    for action in lst_fixed:
        service.add_action(action, ActionType.FIXED_ACTION)

    for action in lst_rep:
        service.add_action(action, ActionType.REPETITIVE_ACTION)
