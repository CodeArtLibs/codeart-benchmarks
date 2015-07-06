import codeart.benchmarks.servers
import codeart.benchmarks.servers.tornado
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    codeart.benchmarks.servers.disable_logs()
    codeart.benchmarks.servers.tornado.disable_logs()

    from bottle import run
    run(host='0.0.0.0', port=PORT, server='tornado', quiet=True)
