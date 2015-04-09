from bottle import run
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    import meinheld
    meinheld.set_access_logger(None)
    meinheld.set_error_logger(None)
    meinheld.set_keepalive(120)
    import meinheld.server
    meinheld.server.set_access_logger(None)
    import os
    port = int(os.environ.get('PORT', 8000))
    run(host='0.0.0.0', port=port, server='meinheld', quiet=True)
