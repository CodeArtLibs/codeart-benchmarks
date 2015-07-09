import codeart.benchmarks
import codeart.benchmarks.servers as _util
import codeart.benchmarks.servers._tornado as _tornado
from codeart.benchmarks._tornado import *


_util.disable_logs()
_tornado.disable_logs()


import tornado.wsgi
app = tornado.wsgi.WSGIAdapter(app)
