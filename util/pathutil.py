from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent


def get_resource_path():
    return "{}/resource".format(get_project_root())
