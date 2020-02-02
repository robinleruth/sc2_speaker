from dataclasses import dataclass
from typing import Union

from app.domain.service.param.param_name import ParamName


@dataclass
class Param:
    name: ParamName
    value: Union[int, str, float]
