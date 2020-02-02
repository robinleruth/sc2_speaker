from abc import ABCMeta
from abc import abstractmethod

from app.domain.service.param.param_name import ParamName
from app.domain.model.param import Param


class ParamConnector(metaclass=ABCMeta):
    @abstractmethod
    def get_param(self, param_name: ParamName) -> Param:
        pass
