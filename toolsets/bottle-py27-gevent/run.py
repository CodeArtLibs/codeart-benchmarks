from gevent import monkey; monkey.patch_all()
from bottle import run
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 8000))
    run(host='0.0.0.0', port=port, server='gevent', quiet=True)