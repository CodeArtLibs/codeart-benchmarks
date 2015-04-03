import falcon

from codeart.benchmarks import *


def version():
    pass


class Request1kb(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        response.body = response1kb()

class Request100kb(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        response.body = response100kb()

class Request1mb(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        response.body = response1mb()

class Request1s(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        response.body = responseSleep1s()

class RequestJson(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_JSON)
        response.body = responseJson()

class RequestHtml(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_HTML)
        response.body = responseHtml()

class RequestDBcreate(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        response.body = OK

class RequestDBread(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        response.body = OK

class RequestDBcrud(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', CONTENT_TYPE_PLAIN)
        response.body = OK


app = falcon.API()
app.add_create("/1kb-response", Request1kb())
app.add_create("/100kb-response", Request100kb())
app.add_create("/1mb-response", Request1mb())
app.add_create("/1s-response", Request1s())
app.add_create("/json-response", RequestJson())
app.add_create("/html-response", RequestHtml())
app.add_create("/db-create", RequestDBcreate())
app.add_create("/db-read", RequestDBread())
app.add_create("/db-crud", RequestDBcrud())

