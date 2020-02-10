import pandas as pd

from app.domain.model.action import Action
from app.domain.service.main_service import MainService
from app.domain.service.action_type import ActionType


if __name__ == '__main__':
    lst_fixed = [Action(time=0, name="Let's go bro !"),
                 Action(time=2, name="Make drone"),
                 Action(time=4, name="Scout for expand")]

    lst_rep = [Action(time=0, name="creep"),
               Action(time=0, name="inject")]

    service = MainService()

    for action in lst_fixed:
        service.add_action(action, ActionType.FIXED_ACTION)

    for action in lst_rep:
        service.add_action(action, ActionType.REPETITIVE_ACTION)
