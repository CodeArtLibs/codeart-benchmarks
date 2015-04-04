import falcon

from codeart.benchmarks import *


def version():
    return falcon.__version__


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
app.add_route("/1kb-response", Request1kb())
app.add_route("/100kb-response", Request100kb())
app.add_route("/1mb-response", Request1mb())
app.add_route("/1s-response", Request1s())
app.add_route("/json-response", RequestJson())
app.add_route("/html-response", RequestHtml())
app.add_route("/db-create", RequestDBcreate())
app.add_route("/db-read", RequestDBread())
app.add_route("/db-crud", RequestDBcrud())
