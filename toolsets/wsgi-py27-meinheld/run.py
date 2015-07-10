import codeart.benchmarks
import codeart.benchmarks.servers as _util
import codeart.benchmarks.servers._meinheld as _meinheld
from codeart.benchmarks._wsgi import *
from codeart.benchmarks.responses import *


if __name__ == '__main__':
    _util.disable_logs()
    _meinheld.disable_logs()
    _meinheld.configure()

    from meinheld import server
    server.listen(('0.0.0.0', _util.get_port()))
    server.run(app)
