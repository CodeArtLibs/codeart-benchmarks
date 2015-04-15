from codeart.benchmarks._wheezy_web import *


import meinheld
meinheld.set_access_logger(None)
meinheld.set_error_logger(None)
meinheld.set_keepalive(120)
import meinheld.server
meinheld.server.set_access_logger(None)
