from gevent import monkey; monkey.patch_all()

from bottle import run

import codeart.benchmarks
import codeart.benchmarks.servers as _util
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    _util.disable_logs()

    run(host='0.0.0.0', port=_util.get_port(), server='gevent', quiet=True, log=None)
