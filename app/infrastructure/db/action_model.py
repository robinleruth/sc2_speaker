from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.infrastructure.db import Base


class Action(Base):
    __tablename__ = 'action'

    id = Column(Integer, primary_key=True)
    time = Column(Float)
    name = Column(String)
    action_type = Column(String)

    def __repr__(self):
        return '<{} : Action {} - {}>'.format(str(self.id), str(self.time), self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'time': self.time,
            'name': self.name,
            'action_type': self.action_type
        }
