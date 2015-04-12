from codeart.benchmarks._tornado import *
import tornado.wsgi


app = tornado.wsgi.WSGIAdapter(app)
