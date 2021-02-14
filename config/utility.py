import yaml
from util import pathutil
from config.envconfig import get_profile


def get_config(alias):
    """
    Return config for a given alias.

    Example: If alias = "redis",
             then seek realm config file redis-<profile>.yaml
             If found,      return content as config.
             If not  found, seek generic config file redis.yaml and
             return content as config.

    :raise FileNotFoundError if neither config files exists.
    """
    try:
        config = __read_realm_config(alias)
    except FileNotFoundError:
        # If generic config is also not found, crash the application :)
        config = __read_generic_config(alias)
    return config


def __read_realm_config(alias):
    configfile = "{}/{}-{}.yaml".format(
        pathutil.get_resource_path(), alias, get_profile())
    return __read_config_from_file(configfile)


def __read_generic_config(alias):
    configfile = "{}/{}.yaml".format(pathutil.get_resource_path(), alias)
    return __read_config_from_file(configfile)


def __read_config_from_file(configfile):
    with open(configfile, 'r') as cf:
        config = yaml.safe_load(cf.read())
    return config
