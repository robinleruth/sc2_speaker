from typing import List

from app.domain.service.param.param_connector import ParamConnector
from app.domain.service.param.param_name import ParamName
from app.domain.model.param import Param
from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.param_model import Param as ParamDb
from app.infrastructure.log import logger


class DbParamConnector(ParamConnector):
    def get_param(self, param_name: ParamName) -> Param:
        with transaction_context() as session:
            entry = session.query(ParamDb).filter_by(name=param_name.value).first()
            if entry is None:
                logger.error(f'{param_name} not in db')
                raise Exception(f'{param_name} not in db')
            param = Param(name=param_name, value=entry.value)
        return param

    def add_param(self, name: str, value):
        param_name = ParamName(name)
        if param_name is ParamName.OTHER:
            logger.error(f'{name} not in ParamName enum')
            raise Exception(f'{name} not in ParamName enum. Accepted value : ' + ';'.join([i for i in ParamName]))
        with transaction_context() as session:
            entry = ParamDb(name=param_name, value=value)
            session.add(entry)

    def delete_param(self, param_name: ParamName):
        with transaction_context() as session:
            entry = session.query(ParamDb).filter_by(name=param_name.value).first()
            if entry is not None:
                session.delete(entry)

    def get_all(self) -> List[Param]:
        with transaction_context() as session:
            lst = session.query(ParamDb).all()
            lst = [Param(name=i.name, value=i.value) for i in lst]
        return lst
