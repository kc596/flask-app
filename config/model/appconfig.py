from config.utility import get_config


class AppConfig:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.dc = kwargs["dc"]
        self.version = kwargs["version"]
        pass

    def __str__(self):
        return "AppConfig={}".format(vars(self))

    @staticmethod
    def load():
        app_config = get_config("config")
        return AppConfig(
            name=app_config["name"],
            dc=app_config["dc"],
            version=app_config["version"])
