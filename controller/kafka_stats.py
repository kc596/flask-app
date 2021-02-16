from http import HTTPStatus
from log.kafkalog import get_total_count, get_failure_count, get_success_count


def kafka_stats():
    """ Controller for getting kafka stats """
    response = {
        "total": get_total_count(),
        "success": get_success_count(),
        "failed": get_failure_count()
    }
    return response, HTTPStatus.OK
