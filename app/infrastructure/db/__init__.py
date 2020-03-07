from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from app.infrastructure.config import app_config


Base = declarative_base()

engine = create_engine(app_config.SQL_URI, connect_args={'check_same_thread': False})
Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=True))

from .action_model import Action
from .param_model import Param
from .log import Log
Base.metadata.create_all(engine)
