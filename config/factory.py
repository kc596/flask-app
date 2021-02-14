import copy
from config.model.appconfig import AppConfig


"""
Factory to get all the configs.
"""


_app_config = AppConfig.load()


def get_app_config():
    return copy.deepcopy(_app_config)
