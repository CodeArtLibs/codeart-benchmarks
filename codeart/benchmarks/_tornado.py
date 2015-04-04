import tornado
import tornado.ioloop
import tornado.web
import tornado.gen

from codeart.benchmarks import *


def version():
    return tornado.version


class Request1kb(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        self.write(response1kb())

class Request100kb(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        self.write(response100kb())

class Request1mb(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        self.write(response1mb())

class Request1s(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        self.write(responseSleep1s())

class RequestJson(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_JSON)
        self.write(responseJson())

class RequestHtml(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_HTML)
        self.write(responseHtml())


class RequestDBcreate(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        mongoengine_create()
        self.write(OK)

class RequestDBread(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        mongoengine_read()
        self.write(OK)

class RequestDBcrud(tornado.web.RequestHandler):
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        mongoengine_crud()
        self.write(OK)


class RequestDBcreateAsync(tornado.web.RequestHandler):
    @gen.coroutine
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        yield motorengine_create()
        self.write(OK)

class RequestDBreadAsync(tornado.web.RequestHandler):
    @gen.coroutine
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        yield motorengine_read()
        self.write(OK)

class RequestDBcrudAsync(tornado.web.RequestHandler):
    @gen.coroutine
    def on_get(self, request, response):
        self.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        yield motorengine_crud()
        self.write(OK)


app = tornado.web.Application([
    (r"/1kb-response", Request1kb),
    (r"/100kb-response", Request100kb),
    (r"/1mb-response", Request1mb),
    (r"/1s-response", Request1s),
    (r"/json-response", RequestJson),
    (r"/html-response", RequestHtml),
    (r"/db-create", RequestDBcreate),
    (r"/db-read", RequestDBread),
    (r"/db-crud", RequestDBcrud),
])
