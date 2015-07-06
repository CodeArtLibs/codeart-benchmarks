import logging


def disable_logs():
    for n in ['tornado', 'tornado.access', 'tornado.application']:
        logger = logging.getLogger(n)
        logger.setLevel(logging.CRITICAL)
        logger.disabled = True
        logger.propagate = False
