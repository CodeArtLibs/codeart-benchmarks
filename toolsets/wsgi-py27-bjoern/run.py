import codeart.benchmarks.servers
from codeart.benchmarks._wsgi import *
from codeart.benchmarks.requests import *


codeart.benchmarks.servers.disable_logs()


if __name__ == "__main__":
    import bjoern
    bjoern.listen(app, 'localhost', get_port(), reuse_port=True)
    bjoern.run()
