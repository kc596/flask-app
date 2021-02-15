import logging.config
from app import app
from config.factory import get_log_config


# setup
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
logging.config.dictConfig(get_log_config())


if __name__ == '__main__':
    app.run()   # start local flask development server
