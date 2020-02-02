import unittest

from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.action_model import Action


class TestDb(unittest.TestCase):
    def setUp(self):
        print('Begin test fixed action service')

    def tearDown(self):
        print('End test fixed action service')

    def test_db(self):
        with transaction_context() as session:
            lst = session.query(Action).all()
        for i in lst:
            print(i)


if __name__ == '__main__':
    unittest.main(verbosity=2)
