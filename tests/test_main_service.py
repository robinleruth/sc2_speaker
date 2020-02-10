import time
import unittest

from app.domain.service.main_service import MainService
from app.domain.service.action_type import ActionType
from app.infrastructure.connector.test_action_connector import TestActionConnector
from app.infrastructure.connector.test_repetitive_action_connector import TestRepetitiveActionConnector
from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.action_model import Action


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

    def test_main_service_db_connection(self):
        with transaction_context() as session:
            entry = Action(time=1, name="test1", action_type=ActionType.FIXED_ACTION.value)
            session.add(entry)
            entry = Action(time=2, name="test2", action_type=ActionType.FIXED_ACTION.value)
            session.add(entry)
            entry = Action(time=0, name="test3", action_type=ActionType.REPETITIVE_ACTION.value)
            session.add(entry)
        service = MainService()
        service.run()
        lst = service.get_action_from_queue()
        self.assertEqual(len(lst), 0)
        time.sleep(3)
        lst = service.get_action_from_queue()
        self.assertEqual(len(lst), 3)
        with transaction_context() as session:
            lst = session.query(Action).all()
            for i in lst:
                print(i)
                session.delete(i)


if __name__ == '__main__':
    unittest.main(verbosity=2)
