from enum import Enum


class ActionType(str, Enum):
    REPETITIVE_ACTION = 'repetitive_action'
    FIXED_ACTION = 'fixed_action'
    OTHER = 'other'

    @classmethod
    def _missing_(cls, value):
        return ActionType.OTHER
