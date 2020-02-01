from abc import ABCMeta
from abc import abstractmethod
from typing import List

from app.domain.model.action import Action


class ActionConnector(metaclass=ABCMeta):
    @abstractmethod
    def get_action_list() -> List[Action]:
        pass
