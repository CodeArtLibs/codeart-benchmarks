from codeart.benchmarks._falcon import *

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
