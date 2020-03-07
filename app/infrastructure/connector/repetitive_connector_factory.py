from app.domain.service.action_connector import ActionConnector
from app.infrastructure.config import app_config
from app.infrastructure.config import TestConfig
from app.infrastructure.connector.test_repetitive_action_connector import TestRepetitiveActionConnector
from app.infrastructure.connector.db_repetitive_action_connector import DbRepetitiveActionConnector


def repetitive_connector_factory() -> ActionConnector:
    if app_config == TestConfig:
        return TestRepetitiveActionConnector()
    else:
        return DbRepetitiveActionConnector()
