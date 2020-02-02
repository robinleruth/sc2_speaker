import time
import unittest

from threading import Thread
from queue import Queue

from app.domain.service.repetitive_action_service import RepetitiveActionService
from app.infrastructure.connector.test_repetitive_action_connector import TestRepetitiveActionConnector


class TestRepetitiveActionService(unittest.TestCase):
    def setUp(self):
        print('BEGIN TestRepetitiveActionService')

    def tearDown(self):
        print('END TestRepetitiveActionService')

    def test_repetitive_action_service(self):
        queue = Queue()
        connector = TestRepetitiveActionConnector()
        service = RepetitiveActionService(shared_queue=queue,
                                          action_connector=connector)
        service.repetitive_time = 3
        service.begin_time = 0
        # service.run()
        t = Thread(target=service)
        t.setDaemon(True)
        t.start()
        time.sleep(1)
        self.assertEqual(len(service.actions), 2)
        self.assertEqual(queue.qsize(), 2)
        time.sleep(3)
        self.assertEqual(len(service.actions), 2)
        self.assertEqual(queue.qsize(), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
