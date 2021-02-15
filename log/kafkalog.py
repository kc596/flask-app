import logging
import threading
from kafka import KafkaProducer


_producer = None
_lock_init = threading.Lock()
_lock_success, _lock_failure = threading.Lock(), threading.Lock()
_success_count = 0
_failure_count = 0


def get_success_count():
    return _success_count


def get_failure_count():
    return _failure_count


def _get_producer(bootstrap_servers, retries):
    global _producer
    if _producer is None:
        with _lock_init:
            if _producer is None:
                print(bootstrap_servers, retries)
                _producer = KafkaProducer(
                    bootstrap_servers=bootstrap_servers,
                    retries=retries,
                    value_serializer=lambda m: m.encode('utf-8'))
    return _producer


def _on_success(record_metadata):
    global _success_count
    with _lock_success:
        _success_count += 1


def _on_error(exception):
    global _failure_count
    with _lock_failure:
        _failure_count += 1


class KafkaLogHandler(logging.Handler):
    def __init__(self, bootstrap_servers, retries, topic, *args, **kwargs):
        logging.Handler.__init__(self, *args, **kwargs)
        self.producer = _get_producer(bootstrap_servers, retries)
        self.topic = topic

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        self.producer.send(topic=self.topic, value=msg).add_callback(
            _on_success).add_errback(_on_error)

    def flush(self):
        self.producer.flush(timeout=10)

    def close(self):
        if self.producer:
            self.producer.close()
