import logging
import os


def disable_logs():
    logging.disable(logging.CRITICAL)
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)
    logger.disabled = True
    logger.propagate = False


def get_server():
    return os.getenv('SERVER', None)


def get_port():
    return int(os.environ.get('PORT', 8000))
