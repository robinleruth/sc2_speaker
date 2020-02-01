import os


class Config:
    SQL_URI = 'sqlite:///app.db'


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass
