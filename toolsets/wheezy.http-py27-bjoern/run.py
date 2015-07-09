import codeart.benchmarks
import codeart.benchmarks.servers as _util
from codeart.benchmarks._wheezy_http import *


if __name__ == "__main__":
    _util.disable_logs()

    import bjoern
    bjoern.listen(app, 'localhost', _util.get_port(), reuse_port=True)
    bjoern.run()
