from app.domain.service.param.param_connector import ParamConnector
from app.domain.service.param.param_name import ParamName
from app.domain.model.param import Param
from app.infrastructure.db.db_session import transaction_context
from app.infrastructure.db.param_model import Param as ParamDb


class DbParamConnector(ParamConnector):
    def get_param(self, param_name: ParamName) -> Param:
        with transaction_context() as session:
            entry = session.query(ParamDb).filter_by(name=param_name.value).first()
            if entry is None:
                raise Exception(f'{param_name} not in db')
            param = Param(name=param_name, value=entry.value)
        return param

