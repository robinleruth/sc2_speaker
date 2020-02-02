from enum import Enum


class ParamName(str, Enum):
    BEGIN_TIME_REPETITIVE_ACTION = 'BEGIN_TIME_REPETITIVE_ACTION'
    OTHER = 'other'

    @classmethod
    def _missing_(cls, value):
        return ParamName.OTHER

