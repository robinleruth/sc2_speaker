from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.sql import func

from app.infrastructure.db import Base


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    logger = Column(String)
    level = Column(String)
    trace = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=func.now())

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log {} {}>".format(self.created_at.strftime('%Y-%m-%d'),
                                    self.message[:50])
