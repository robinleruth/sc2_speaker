import unittest

from app.domain.service.param.param_service import ParamService
from app.domain.service.param.param_name import ParamName
from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.param_model import Param as ParamDb


class TestParamService(unittest.TestCase):
    def setUp(self):
        print('BEGIN TestParamService')
        with transaction_context() as session:
            entry = ParamDb(name=ParamName.BEGIN_TIME_REPETITIVE_ACTION, value=2)
            print(f'{entry} added to db')
            session.add(entry)

    def tearDown(self):
        print('END TestParamService')
        with transaction_context() as session:
            lst = session.query(ParamDb).all()
            for elem in lst:
                session.delete(elem)
                print(f'{elem} removed from db')

    def test_param_service(self):
        service = ParamService()
        param = service.get_param(ParamName.BEGIN_TIME_REPETITIVE_ACTION)
        print(f'{param} found !')


if __name__ == '__main__':
    unittest.main(verbosity=2)
