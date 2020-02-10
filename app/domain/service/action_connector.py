from abc import ABCMeta
from abc import abstractmethod
from typing import List

from app.domain.model.action import Action


class ActionConnector(metaclass=ABCMeta):
    @abstractmethod
    def get_action_list(self) -> List[Action]:
        pass

    @abstractmethod
    def persist_entry(self, action: Action):
        pass

    @abstractmethod
    def delete_entry(self, action: Action):
        pass
