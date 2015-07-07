import codeart.benchmarks.servers as _util
import codeart.benchmarks.servers._meinheld as _meinheld
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    _util.disable_logs()
    _meinheld.disable_logs()
    _meinheld.configure()

    from bottle import run
    run(host='0.0.0.0', port=_util.get_port(), server='meinheld', quiet=True)
