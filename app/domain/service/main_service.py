from queue import Queue
from dataclasses import dataclass

from app.domain.service.fixed_action_service import FixedActionService
from app.domain.service.action_connector import ActionConnector


class MainService:
    fixed_action_service: FixedActionService

    def __init__(self, fixed_action_connector: ActionConnector):
        self.queue = Queue()
        self.fixed_action_service = FixedActionService(fixed_action_connector,
                                                       queue)

    def run(self):
        # Create some thread class in infrastructure to have some parallelism!
        pass
