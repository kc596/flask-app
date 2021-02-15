from log.constants import *


"""
All the log object using `jsonlogger` will have fields mentioned in FORMAT.
    key: string, the key of json log.
    value: `LogRecord` attribute name.

Example: key=F, value=filename. The log will be like :
{...
    "F": "/somedir/somefile.ext",
...}
"""

RECORD_CUSTOM_ATTRS = {
    "levelname": lambda **record_attrs: record_attrs["levelname"] if record_attrs['levelname'] in [
        'DEBUG',
        'INFO',
        'WARN',
        'WARNING',
        'NOTSET',
        'ERROR',
        'CRITICAL'] else None,
}

CUSTOM_FORMAT = dict((
    ("application", "name"),
    ("level", "levelname"),
    ("path", "pathname"),
    ("file", "filename"),
    ("module", "module"),
    ("line", "lineno"),
    ("function", "funcName"),
    ("timestamp", "asctime"),
    ("thread", "threadName"),
    ("process", "process"),
    ("message", "message")
))
