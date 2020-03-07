from app.domain.service.action_connector import ActionConnector
from app.infrastructure.config import app_config
from app.infrastructure.config import TestConfig
from app.infrastructure.connector.test_action_connector import TestActionConnector
from app.infrastructure.connector.db_fixed_action_connector import DbFixedActionConnector


def fixed_connector_factory() -> ActionConnector:
    if app_config == TestConfig:
        return TestActionConnector()
    else:
        return DbFixedActionConnector()
