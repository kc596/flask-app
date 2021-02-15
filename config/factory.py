import copy
from config.model.appconfig import AppConfig
from config.model.logconfig import LogConfig


"""
Factory to get all the configs.
"""


_app_config = AppConfig.load()
_log_config = LogConfig.load()


def get_app_config():
    return copy.deepcopy(_app_config)


def get_log_config():
    return copy.deepcopy(_log_config)
