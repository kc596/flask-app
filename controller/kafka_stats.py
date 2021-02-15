from http import HTTPStatus
from log.kafkalog import get_failure_count, get_success_count


def kafka_stats():
    """ Controller for getting kafka stats """
    response = {
        "success": get_success_count(),
        "failed": get_failure_count()
    }
    return response, HTTPStatus.OK
