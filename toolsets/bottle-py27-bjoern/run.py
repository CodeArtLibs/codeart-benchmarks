import codeart.benchmarks.servers
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    codeart.benchmarks.servers.disable_logs()

    from bottle import run
    run(host='0.0.0.0', port=get_port(), server='bjoern', quiet=True, reuse_port=True)
