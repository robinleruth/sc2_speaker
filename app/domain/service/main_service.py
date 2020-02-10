from queue import Queue
from dataclasses import dataclass
from threading import Thread
from typing import List

from app.domain.service.fixed_action_service import FixedActionService
from app.domain.service.action_connector import ActionConnector
from app.domain.service.repetitive_action_service import RepetitiveActionService
from app.domain.service.action_type import ActionType
from app.domain.model.action import Action
from app.infrastructure.connector.db_repetitive_action_connector import DbRepetitiveActionConnector
from app.infrastructure.connector.db_fixed_action_connector import DbFixedActionConnector
from app.infrastructure.log import logger


class MainService:
    fixed_action_service: FixedActionService
    repetitive_action_service: RepetitiveActionService

    def __init__(self, fixed_action_connector: ActionConnector=DbFixedActionConnector(),
                 repetitive_action_connector: ActionConnector=DbRepetitiveActionConnector()):
        self.queue = Queue()
        self.fixed_action_service = FixedActionService(fixed_action_connector,
                                                       self.queue)
        self.repetitive_action_service = RepetitiveActionService(repetitive_action_connector,
                                                                 self.queue)

    def run(self):
        # Create some thread class in infrastructure to have some parallelism!
        t1 = Thread(target=self.fixed_action_service)
        t2 = Thread(target=self.repetitive_action_service)
        t1.setDaemon(True)
        t2.setDaemon(True)
        t1.start()
        t2.start()

    def get_action_from_queue(self) -> List[Action]:
        lst = []
        while not self.queue.empty():
            lst.append(self.queue.get())
        return lst

    def add_action(self, action: Action, action_type: ActionType):
        if action_type is ActionType.FIXED_ACTION:
            self.fixed_action_service.persist_entry(action)
        elif action_type is ActionType.REPETITIVE_ACTION:
            self.repetitive_action_service.persist_entry(action)
        else:
            raise Exception('Action Type not implemented')

    def delete_action(self, action: Action, action_type: ActionType):
        logger.info('Deleting {}'.format(action))
        if action_type is ActionType.FIXED_ACTION:
            self.fixed_action_service.delete_action(action)
        elif action_type is ActionType.REPETITIVE_ACTION:
            self.repetitive_action_service.delete_action(action)
        else:
            raise Exception('Action Type not implemented')
