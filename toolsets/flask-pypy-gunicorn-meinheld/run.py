import codeart.benchmarks
import codeart.benchmarks.servers as _util
import codeart.benchmarks.servers._meinheld as _meinheld
from codeart.benchmarks._flask import *

# app.config['DEBUG'] = True

_util.disable_logs()
_meinheld.disable_logs()
_meinheld.configure()
