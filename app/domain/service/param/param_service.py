from dataclasses import dataclass
from dataclasses import field
from typing import List

from app.domain.service.param.param_connector import ParamConnector
from app.domain.service.param.param_name import ParamName
from app.domain.model.param import Param
from app.infrastructure.connector.param.db_param_connector import DbParamConnector


@dataclass
class ParamService:
    connector: ParamConnector = field(default_factory=DbParamConnector)

    def get_param(self, param_name: ParamName) -> Param:
        return self.connector.get_param(param_name)

    def add_param(self, name: str, value):
        return self.connector.add_param(name, value)

    def delete_param(self, param_name: ParamName):
        return self.connector.delete_param(param_name)

    def get_all(self) -> List[Param]:
        return self.connector.get_all()
