import logging
import traceback

from app.infrastructure.db.log import Log
from app.infrastructure.db.db_session import transaction_context


class SqlAlchemyHandler(logging.Handler):
    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc()
        with transaction_context() as session:
            log = Log(
                logger=record.__dict__['name'],
                level=record.__dict__['levelname'],
                trace=trace,
                message=record.__dict__['message']
            )
            session.add(log)
