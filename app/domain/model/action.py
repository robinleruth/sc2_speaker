from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Action:
    time: float
    name: str
