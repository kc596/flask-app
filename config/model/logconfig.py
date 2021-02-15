from config.utility import get_config


class LogConfig:
    def __init__(self, **kwargs):
        pass

    def __str__(self):
        return "LogConfig={}".format(vars(self))

    @staticmethod
    def load():
        log_config = get_config("log")
        return log_config
