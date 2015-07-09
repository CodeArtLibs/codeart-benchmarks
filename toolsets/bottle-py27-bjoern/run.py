import codeart.benchmarks
import codeart.benchmarks.servers as _util
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    _util.disable_logs()

    from bottle import run
    run(host='0.0.0.0', port=_util.get_port(), server='bjoern', quiet=True, reuse_port=True)
