from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 8000))

    import logging
    logging.disable(logging.CRITICAL)
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)
    logger.disabled = True
    logger.propagate = False
    for n in ['tornado', 'tornado.access', 'tornado.application']:
        logger = logging.getLogger(n)
        logger.setLevel(logging.CRITICAL)
        logger.disabled = True
        logger.propagate = False

    from bottle import run
    run(host='0.0.0.0', port=port, server='tornado', quiet=True)
