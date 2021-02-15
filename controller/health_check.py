from http import HTTPStatus
from log.logger import get_logger
from log.metriclog import metric_log


@metric_log(key="health-check")
def health_check():
    """ Controller for health check status """
    logger = get_logger()
    logger.info("status", "Application is up and running")
    return "Application is up and running", HTTPStatus.OK
