import codeart.benchmarks.servers
import codeart.benchmarks.servers.meinheld
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    codeart.benchmarks.servers.disable_logs()
    codeart.benchmarks.servers.meinheld.disable_logs()
    codeart.benchmarks.servers.meinheld.configure()

    from bottle import run
    run(host='0.0.0.0', port=PORT, server='meinheld', quiet=True)
