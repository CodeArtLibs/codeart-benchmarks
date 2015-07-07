import codeart.benchmarks.servers as _util
import codeart.benchmarks.servers._meinheld as _meinheld
import codeart.benchmarks.servers._tornado as _tornado
from codeart.benchmarks.__FRAMEWORK import *
from codeart.benchmarks.requests import *


if __name__ == "__main__":
    _util.disable_logs()
    _meinheld.disable_logs()
    _meinheld.configure()
    _tornado.disable_logs()

    if server:
        run(host='0.0.0.0', port=_util.get_port(), server=_util.get_server())
    else:
        run(host='0.0.0.0', port=_util.get_port())
