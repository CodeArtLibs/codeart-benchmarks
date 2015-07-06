import os

import meinheld
import meinheld.server


def disable_logs():
    meinheld.set_access_logger(None)
    meinheld.set_error_logger(None)
    meinheld.server.set_access_logger(None)

def configure():
    meinheld.set_keepalive(int(os.getenv('KEEP_ALIVE', 120))) # timeout in seconds
