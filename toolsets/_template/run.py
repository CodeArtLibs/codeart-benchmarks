import codeart.benchmarks.servers
import codeart.benchmarks.servers.meinheld
import codeart.benchmarks.servers.tornado
from codeart.benchmarks.__FRAMEWORK import *
from codeart.benchmarks.requests import *


if __name__ == "__main__":
    codeart.benchmarks.servers.disable_logs()
    codeart.benchmarks.servers.meinheld.disable_logs()
    codeart.benchmarks.servers.meinheld.configure()
    codeart.benchmarks.servers.tornado.disable_logs()

    if server:
        run(host='0.0.0.0', port=PORT, server=SERVER)
    else:
        run(host='0.0.0.0', port=PORT)
