import time
import unittest

from app.domain.service.main_service import MainService
from app.infrastructure.connector.test_action_connector import TestActionConnector
from app.infrastructure.connector.test_repetitive_action_connector import TestRepetitiveActionConnector


class TestMainService(unittest.TestCase):
    def setUp(self):
        print('Begin test main service')

    def tearDown(self):
        print('End test main service')

    def test_main_service(self):
        fixed_connector = TestActionConnector()
        repetitive_connector = TestRepetitiveActionConnector()
        service = MainService(fixed_connector, repetitive_connector)
        service.run()
        lst = service.get_action_from_queue()
        self.assertEqual(len(lst), 0)
        time.sleep(3)
        lst = service.get_action_from_queue()
        print(lst)
        self.assertEqual(len(lst), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
