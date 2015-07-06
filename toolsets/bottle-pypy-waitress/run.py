import codeart.benchmarks.servers
from codeart.benchmarks._bottle import *


codeart.benchmarks.servers.disable_logs()


# if __name__ == "__main__":
#     import logging
#     logger = logging.getLogger('waitress')
#     logger.setLevel(logging.CRITICAL)
#     logger.disabled = True
#     logger.propagate = False

#     run(host='0.0.0.0', port=PORT, server='waitress', quiet=True)
