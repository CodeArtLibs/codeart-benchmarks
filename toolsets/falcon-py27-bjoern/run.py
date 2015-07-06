import codeart.benchmarks.servers
from codeart.benchmarks._falcon import *


if __name__ == "__main__":
    codeart.benchmarks.servers.disable_logs()

    import bjoern
    bjoern.listen(app, 'localhost', get_port(), reuse_port=True)
    bjoern.run()
