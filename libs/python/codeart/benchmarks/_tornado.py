import tornado
import tornado.ioloop
import tornado.web
from tornado import gen

from codeart.benchmarks import *


def version():
    return tornado.version


class Request1kb(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        self.write(response_1kb())

class Request100kb(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        self.write(response_100kb())

class Request1mb(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        self.write(response_1mb())

class RequestJson(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        self.write(response_json())

class RequestHtml(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_HTML)
        self.write(response_html())

class RequestSlow(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        self.write(response_slow())


class RequestDBread(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        self.write(response_db_read_queries())

class RequestDBwrite(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        self.write(response_db_write_queries())


class RequestCacheRead(tornado.web.RequestHandler):
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        self.write(response_cached())


app = tornado.web.Application([
    (r'/', RequestHtml),
    (r'/1kb-response', Request1kb),
    (r'/100kb-response', Request100kb),
    (r'/1mb-response', Request1mb),
    (r'/json-response', RequestJson),
    (r'/html-response', RequestHtml),
    (r'/slow-response', RequestSlow),
    (r'/db-read', RequestDBread),
    (r'/db-write', RequestDBwrite),
    (r'/cache-read', RequestCacheRead),
])
