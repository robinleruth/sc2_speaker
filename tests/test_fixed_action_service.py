import unittest
from queue import Queue

from app.domain.service.fixed_action_service import FixedActionService
from app.infrastructure.connector.test_action_connector import TestActionConnector


class TestFixedActionService(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_service(self):
        print('Begin')
        queue = Queue()
        connector = TestActionConnector()
        service = FixedActionService(action_connector=connector,
                                     shared_queue=queue)
        service.run()
        while not queue.empty():
            print(queue.get())
        self.assertEqual(True, True)
        print('Done')


if __name__ == '__main__':
    unittest.main(verbosity=2)

