import codeart.benchmarks
import codeart.benchmarks.servers as _util

import pyximport; pyximport.install()
import _wsgi_cython

_util.disable_logs()


if __name__ == "__main__":
    import bjoern
    bjoern.listen(_wsgi_cython.app, 'localhost', _util.get_port(), reuse_port=True)
    bjoern.run()
