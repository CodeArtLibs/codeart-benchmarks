import codeart.benchmarks.servers
import codeart.benchmarks.servers.tornado
from codeart.benchmarks._tornado import *


codeart.benchmarks.servers.disable_logs()
codeart.benchmarks.servers.tornado.disable_logs()


import tornado.wsgi
app = tornado.wsgi.WSGIAdapter(app)
