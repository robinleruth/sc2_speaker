from queue import Queue
from dataclasses import dataclass
from threading import Thread
from typing import List

from app.domain.service.fixed_action_service import FixedActionService
from app.domain.service.action_connector import ActionConnector
from app.domain.model.action import Action


class MainService:
    fixed_action_service: FixedActionService

    def __init__(self, fixed_action_connector: ActionConnector):
        self.queue = Queue()
        self.fixed_action_service = FixedActionService(fixed_action_connector,
                                                       self.queue)

    def run(self):
        # Create some thread class in infrastructure to have some parallelism!
        t1 = Thread(target=self.fixed_action_service)
        t1.start()

    def get_action_from_queue(self) -> List[Action]:
        lst = []
        while not self.queue.empty():
            lst.append(self.queue.get())
        return lst
