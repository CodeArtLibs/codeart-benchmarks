import falcon

from codeart.benchmarks import *


def version():
    return falcon.__version__


class Request1kb(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        response.body = response_1kb()

class Request100kb(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        response.body = response_100kb()

class Request1mb(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        response.body = response_1mb()

class RequestJson(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        response.body = response_json()

class RequestHtml(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_HTML)
        response.body = response_html()

class RequestSlow(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        response.body = response_slow()


class RequestDBread(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        response.body = response_db_read_queries()

class RequestDBwrite(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
        response.body = response_db_write_queries()


class RequestCacheRead(object):
    def on_get(self, request, response):
        response.set_header(CONTENT_TYPE, CONTENT_TYPE_PLAIN)
        response.body = response_cached()


app = falcon.API()
app.add_route('/', RequestHtml())
app.add_route('/1kb-response', Request1kb())
app.add_route('/100kb-response', Request100kb())
app.add_route('/1mb-response', Request1mb())
app.add_route('/json-response', RequestJson())
app.add_route('/html-response', RequestHtml())
app.add_route('/slow-response', RequestSlow())
app.add_route('/db-read', RequestDBread())
app.add_route('/db-write', RequestDBwrite())
app.add_route('/cache-read', RequestCacheRead())
