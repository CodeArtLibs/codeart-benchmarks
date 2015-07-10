import tornado
import tornado.ioloop
import tornado.web
from tornado import gen

from codeart.benchmarks import *


def version():
    return tornado.version


class Request1kb(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        self.write(response_1kb())

class Request100kb(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        self.write(response_100kb())

class Request1mb(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        self.write(response_1mb())

class RequestJson(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        self.write(response_json())

class RequestHtml(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_HTML)
        self.write(response_html())

class RequestSlow(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        yield gen.sleep(RESPONSE_SLOW)
        self.write(RESPONSE_SLOW_MSG)


class RequestDBread(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        response = yield gen.maybe_future(response_db_read_queries())
        self.write(response)

class RequestDBwrite(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        response = yield gen.maybe_future(response_db_write_queries())
        self.write(response)


class RequestCacheRead(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        response = yield gen.maybe_future(response_cached())
        self.write(response)


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
