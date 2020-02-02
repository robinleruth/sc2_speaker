import time

from dataclasses import dataclass
from dataclasses import field
from queue import Queue

from app.domain.service.action_service import ActionService
from app.domain.service.param.param_service import ParamService
from app.domain.service.param.param_name import ParamName
from app.infrastructure.log import logger


@dataclass
class RepetitiveActionService(ActionService):
    begin_time: float = 1
    repetitive_time: float = 40 # in seconds
    param_service: ParamService = field(default_factory=ParamService)

    def go(self):
        logger.info('RepetitiveActionService go !')
        try:
            param = self.param_service.get_param(ParamName.BEGIN_TIME_REPETITIVE_ACTION)
            self.begin_time = float(param.value)
        except:
            pass
        try:
            param = self.param_service.get_param(ParamName.REPETITIVE_INTERVAL)
            self.repetitive_time = float(param.value)
        except:
            pass
        self.populate_action_list()
        self.start_time = time.time()
        while True:
            if time.time() - self.start_time < self.begin_time:
                continue
            self.populate_queue()
            time.sleep(self.repetitive_time)

    def populate_action_list(self):
        self.actions = self.action_connector.get_action_list()
        logger.info('RepetitiveActionService actions : ' + str(self.actions))

    def populate_queue(self):
        for action in self.actions:
            self.shared_queue.put(action)
