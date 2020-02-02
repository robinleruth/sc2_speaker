from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Integer

from app.infrastructure.db import Base


class Param(Base):
    __tablename__ = 'param'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)

    def __repr__(self):
        return '<Param {} - {}>'.format(self.name, self.value)
