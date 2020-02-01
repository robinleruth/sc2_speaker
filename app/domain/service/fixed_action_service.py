from queue import Queue
from dataclasses import field
from typing import List
import time

from app.domain.service.action_service import ActionService
from app.domain.model.action import Action
from app.infrastructure.log import logger


class FixedActionService(ActionService):
    queue: Queue = field(default_factory=Queue)

    def go(self):
        logger.info('FixedActionService go !')
        self.populate_queue()
        while not self.queue.empty():
            action: Action = self.queue.get()
            logger.info(f'Getting action : {action}')
            while self.elapsed_time < action.time:
                self.elapsed_time = time.time() - self.start_time
            self.shared_queue.put(action)

    def populate_queue(self):
        logger.info('populate_queue')
        lst: List[Action] = self.action_connector.get_action_list()
        self.actions = sorted(lst, key=lambda x: x.time)
        logger.info('Get action list : ' + self.actions)
        for elem in self.actions:
            self.queue.put(elem)
