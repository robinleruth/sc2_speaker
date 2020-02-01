import os


class Config:
    SQL_URI = 'sqlite:///app.db'
    LOG_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs')
    LOG_FILENAME = 'app.log'
    LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILENAME)


app_config = Config
