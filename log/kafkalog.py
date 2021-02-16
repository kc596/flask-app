import logging
import threading
from confluent_kafka import Producer


_producer = None
_lock_init = threading.Lock()
_lock_t, _lock_s, _lock_f = threading.Lock(), threading.Lock(), threading.Lock()
_total_count, _success_count, _failure_count = 0, 0, 0


# Exposing kafka logging stats
def get_total_count():
    return _total_count


def get_success_count():
    return _success_count


def get_failure_count():
    return _failure_count


class KafkaLogHandler(logging.Handler):
    def __init__(self, bootstrap_servers: str, topic: str, *args, **kwargs):
        logging.Handler.__init__(self, *args, **kwargs)
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer = None

    @staticmethod
    def _get_producer(bootstrap_servers):
        global _producer
        if _producer is None:
            with _lock_init:
                if _producer is None:
                    _producer = Producer(
                        {"bootstrap.servers": bootstrap_servers})
        return _producer

    def emit(self, record: logging.LogRecord) -> None:
        if self.producer is None:
            self.producer = self._get_producer(self.bootstrap_servers)
        with _lock_t:
            global _total_count
            _total_count += 1
        msg = self.format(record)
        self.producer.produce(
            topic=self.topic,
            value=msg,
            callback=self.delivery_report)
        self.producer.poll(0)

    @staticmethod
    def delivery_report(err, msg):
        """
        Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush().
        """
        if err is not None:
            with _lock_f:
                global _failure_count
                _failure_count += 1
        else:
            with _lock_s:
                global _success_count
                _success_count += 1

    def flush(self):
        self.producer.flush()

    def close(self):
        global _producer
        _producer = None
        pass
