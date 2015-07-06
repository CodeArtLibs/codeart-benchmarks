import logging


def disable_logs():
    logging.disable(logging.CRITICAL)
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)
    logger.disabled = True
    logger.propagate = False


SERVER = os.getenv('SERVER', None)
PORT = int(os.environ.get('PORT', 8000))
