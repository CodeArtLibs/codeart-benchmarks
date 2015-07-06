from gevent import monkey; monkey.patch_all()
from bottle import run
import codeart.benchmarks.servers
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    codeart.benchmarks.servers.disable_logs()

    run(host='0.0.0.0', port=PORT, server='gevent', quiet=True, log=None)
