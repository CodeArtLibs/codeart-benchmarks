from bottle import run
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    # evwsgi.set_debug(0)

    import os
    port = int(os.environ.get('PORT', 8000))
    run(host='0.0.0.0', port=port, server='fapws3', quiet=True)
