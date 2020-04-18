from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.infrastructure.db import Base


class BuildOrder(Base):
    __tablename__ = 'build'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    actions = relationship('Action', backref='build_order', cascade="all,delete", lazy='dynamic')

    def __repr__(self):
        return '<{} : BuildOrder {}>'.format(str(self.id), str(self.name))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
