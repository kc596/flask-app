from config.envconfig import get_build_version
from config.utility import get_config


class AppConfig:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.dc = kwargs["dc"]
        self.version = kwargs["version"]
        self.build_version = kwargs["build_version"]

    def __str__(self):
        return "AppConfig={}".format(vars(self))

    @staticmethod
    def load():
        # yaml file configs
        app_config = get_config("config")

        # env configs
        build_version = get_build_version()

        return AppConfig(
            name=app_config["name"],
            dc=app_config["dc"],
            version=app_config["version"],
            build_version=build_version
        )
