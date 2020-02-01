from queue import Queue
from dataclasses import field
from typing import List
import time

from app.domain.service.action_service import ActionService
from app.domain.model.action import Action


class FixedActionService(ActionService):
    queue: Queue = field(default_factory=Queue)

    def go(self):
        self.populate_queue()
        while not self.queue.empty():
            action: Action = self.queue.get()
            while self.elapsed_time < action.time:
                self.elapsed_time = time.time() - self.start_time
            self.shared_queue.put(action)

    def populate_queue(self):
        lst: List[Action] = self.action_connector.get_action_list()
        self.actions = sorted(lst, key=lambda x: x.time)
        for elem: Action in self.actions:
            self.queue.put(elem)
