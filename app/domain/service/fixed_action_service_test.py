from unittest import TestCase
from queue import Queue

from app.domain.service.fixed_action_service import FixedActionService
from app.domain.service.test_action_connector import TestActionConnector


class FixedActionServiceTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_service(self):
        queue = Queue()
        connector = TestActionConnector()
        service = FixedActionService(action_connector=connector,
                                     shared_queue=queue)
