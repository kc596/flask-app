from http import HTTPStatus


def health_check():
    """ Controller for health check status """
    return "Application is up and running", HTTPStatus.OK
