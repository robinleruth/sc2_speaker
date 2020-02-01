import time

from abc import ABCMeta
from abc import abstractmethod
from typing import List
from queue import Queue
from threading import Thread
from dataclasses import dataclass
from dataclasses import field

from app.domain.model.action import Action
from app.domain.service.action_connector import ActionConnector


@dataclass
class ActionService(Thread, metaclass=ABCMeta):
    action_connector: ActionConnector
    shared_queue: Queue
    start_time: float = time.time()
    elapsed_time: float = 0
    actions: List[Action] = field(default_factory=list)

    def run(self):
        self.go()

    @abstractmethod
    def go(self):
        pass
