import unittest
from queue import Queue

from app.domain.service.fixed_action_service import FixedActionService
from app.infrastructure.connector.test_action_connector import TestActionConnector


class TestFixedActionService(unittest.TestCase):
    def setUp(self):
        print('Begin test fixed action service')

    def tearDown(self):
        print('End test fixed action service')

    def test_service(self):
        queue = Queue()
        connector = TestActionConnector()
        service = FixedActionService(action_connector=connector,
                                     shared_queue=queue)
        service.run()
        while not queue.empty():
            print(queue.get())


if __name__ == '__main__':
    unittest.main(verbosity=2)

