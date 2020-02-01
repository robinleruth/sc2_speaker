import os
import logging

from app.infrastructure.config import app_config


def create_logger():
    _logger = logging.getLogger('sc2_speaker')
    _logger.setLevel(logging.INFO)
    os.makedirs(app_config.LOG_FOLDER, exist_ok=True)
    fh = logging.FileHandler(app_config.LOG_FILE_PATH)
    fmt = '%(asctime)s - %(name)s - %(levelname)s -%(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    _logger.addHandler(fh)
    return _logger


logger = create_logger()
