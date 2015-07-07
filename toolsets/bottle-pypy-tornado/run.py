import codeart.benchmarks.servers as _util
import codeart.benchmarks.servers._tornado as _tornado
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    _util.disable_logs()
    _tornado.disable_logs()

    from bottle import run
    run(host='0.0.0.0', port=_util.get_port(), server='tornado', quiet=True)
