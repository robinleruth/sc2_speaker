from queue import Queue
from dataclasses import dataclass
from threading import Thread
from typing import List

from app.domain.service.fixed_action_service import FixedActionService
from app.domain.service.action_connector import ActionConnector
from app.domain.service.repetitive_action_service import RepetitiveActionService
from app.domain.model.action import Action
from app.infrastructure.connector.db_action_connector import DbFixedActionConnector
from app.infrastructure.connector.db_repetitive_action_connector import DbRepetitiveActionConnector


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
        t2.setDaemon(True)
        t1.start()
        t2.start()

    def get_action_from_queue(self) -> List[Action]:
        lst = []
        while not self.queue.empty():
            lst.append(self.queue.get())
        return lst
