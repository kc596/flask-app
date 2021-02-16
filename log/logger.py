import logging.config
import threading
from config.factory import get_app_config
from jsonformatter import JsonFormatter
from log.jsonlog import CUSTOM_FORMAT, RECORD_CUSTOM_ATTRS
from log.constants import *


class Logger:
    """
    Adapter for enabling logging in the application
    """

    def __init__(self, name):
        self.__log_record = {}
        self.__logger = logging.getLogger(name=name)
        self.__apply_json_formatter()
        self.__set_common_attributes()

    def __apply_json_formatter(self):
        """ changes json log format for all handlers with JsonFormatter """
        formatter = JsonFormatter(
            CUSTOM_FORMAT,
            record_custom_attrs=RECORD_CUSTOM_ATTRS,
            separators=(',', ':'),
            mix_extra=True)
        for handler in self.__logger.parent.handlers:
            if isinstance(handler.formatter, JsonFormatter):
                handler.setFormatter(formatter)

    def __set_common_attributes(self):
        app_config = get_app_config()
        self.__log_record[PROFILE] = app_config.dc
        self.__log_record[BUILD_VERSION] = app_config.build_version

    def id(self, log_id):
        self.__log_record[REQ_ID] = log_id
        return self

    def info(self, key: str, message: str):
        self.__log_record[KEY] = key
        self.__logger.info(msg=message, stacklevel=2, extra=self.__log_record)

    def error(self, key: str, message: str):
        self.__log_record[KEY] = key
        self.__logger.error(msg=message, stacklevel=2, extra=self.__log_record)

    def metric(self, key: str, time: int):
        self.__log_record[KEY] = key
        self.__log_record[TIME] = time
        self.__logger.log(
            level=69,
            msg=None,
            stacklevel=2,
            extra=self.__log_record)

    def raw(self, key: str, request: str, response: str):
        self.__log_record[KEY] = key
        self.__log_record[REQUEST] = request
        self.__log_record[RESPONSE] = response
        self.__logger.log(
            level=69,
            msg=None,
            stacklevel=2,
            extra=self.__log_record)

    def exception(self, err):
        self.__logger.exception(err)


_logger = None
_lock = threading.Lock()


def get_logger():
    global _logger
    if _logger is None:
        with _lock:
            if _logger is None:
                _logger = Logger(get_app_config().name)
    return _logger
