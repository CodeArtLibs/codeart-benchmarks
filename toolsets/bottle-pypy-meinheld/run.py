from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 8000))

    import meinheld
    meinheld.set_access_logger(None)
    meinheld.set_error_logger(None)
    meinheld.set_keepalive(120)
    import meinheld.server
    meinheld.server.set_access_logger(None)

    from bottle import run
    run(host='0.0.0.0', port=port, server='meinheld', quiet=True)
