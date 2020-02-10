from contextlib import contextmanager
from sqlalchemy.orm import scoped_session

from app.infrastructure.db import engine
from app.infrastructure.db import Session


@contextmanager
def transaction_context():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        raise
    finally:
        Session.remove()

