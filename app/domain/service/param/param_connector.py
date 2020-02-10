from abc import ABCMeta
from abc import abstractmethod
from typing import List

from app.domain.service.param.param_name import ParamName
from app.domain.model.param import Param


class ParamConnector(metaclass=ABCMeta):
    @abstractmethod
    def get_param(self, param_name: ParamName) -> Param:
        pass

    @abstractmethod
    def add_param(self, name: str, value):
        pass

    @abstractmethod
    def delete_param(self, param_name: ParamName):
        pass

    @abstractmethod
    def get_all(self) -> List[Param]:
        pass
