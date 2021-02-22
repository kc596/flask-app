import socket
from config.factory import get_app_config
from datetime import datetime, timezone

"""
All the log object using `jsonlogger` will have fields mentioned in FORMAT.
    key: string, the key of json log.
    value: `LogRecord` attribute name.

Example: key=F, value=filename. The log will be like :
{...
    "F": "/somedir/somefile.ext",
...}
"""

appconfig = get_app_config()

RECORD_CUSTOM_ATTRS = {
    "levelname": lambda **record_attrs: record_attrs["levelname"] if record_attrs['levelname'] in [
        'DEBUG',
        'INFO',
        'WARN',
        'WARNING',
        'NOTSET',
        'ERROR',
        'CRITICAL'] else None,
    "env": lambda: appconfig.dc,
    "host": lambda: socket.gethostname(),
    "svr": lambda: appconfig.build_version,
    "timeStamp": lambda: int(
        datetime.now(
            tz=timezone.utc).timestamp()),
}

# These fields are present in all log entries
CUSTOM_FORMAT = dict((
    ("application", "name"),
    ("level", "levelname"),
    ("caller", "pathname"),
    ("file", "filename"),
    ("module", "module"),
    ("line", "lineno"),
    ("function", "funcName"),
    ("timestamp", "asctime"),
    ("thread", "threadName"),
    ("process", "process"),
    ("message", "message"),
    ("host", "host"),
    ("timeStamp", "timeStamp"),
    ("svr", "svr"),
    ("env", "env")
))
