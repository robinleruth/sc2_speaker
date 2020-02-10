import time

from abc import ABCMeta
from abc import abstractmethod
from typing import List
from queue import Queue
from dataclasses import dataclass
from dataclasses import field

from app.domain.model.action import Action
from app.domain.service.action_connector import ActionConnector
from app.infrastructure.log import logger


@dataclass
class ActionService(metaclass=ABCMeta):
    action_connector: ActionConnector
    shared_queue: Queue
    start_time: float = time.time()
    elapsed_time: float = 0
    actions: List[Action] = field(default_factory=list)

    def __call__(self):
        self.run()

    def run(self):
        self.go()

    @abstractmethod
    def go(self):
        pass

    def get_action_list(self) -> List[Action]:
        self.actions = self.action_connector.get_action_list()
        return self.actions

    def persist_entry(self, action: Action):
        logger.info('Persist entry : {}'.format(action))
        self.action_connector.persist_entry(action)

    def delete_action(self, action: Action):
        self.action_connector.delete_entry(action)
        self.actions = self.action_connector.get_action_list()
