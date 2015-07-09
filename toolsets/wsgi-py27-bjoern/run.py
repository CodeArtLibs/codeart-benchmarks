import codeart.benchmarks
import codeart.benchmarks.servers as _util
from codeart.benchmarks._wsgi import *


_util.disable_logs()


if __name__ == "__main__":
    import bjoern
    bjoern.listen(app, 'localhost', _util.get_port(), reuse_port=True)
    bjoern.run()
