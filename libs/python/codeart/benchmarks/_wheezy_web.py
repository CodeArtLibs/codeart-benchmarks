from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory

from codeart.benchmarks import *


def version():
    return wheezy.web.__version__


class Request1kb(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
        response.write(response_1kb())
        return response

class Request100kb(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
        response.write(response_100kb())
        return response

class Request1mb(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
        response.write(response_1mb())
        return response

class RequestJson(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_JSON)]
        response.write(response_json())
        return response

class RequestHtml(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_HTML)]
        response.write(response_html())
        return response

class RequestSlow(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
        response.write(response_slow())
        return response


class RequestDBread(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_JSON)]
        response.write(response_db_read_queries())
        return response

class RequestDBwrite(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_JSON)]
        response.write(response_db_write_queries())
        return response


class RequestCacheRead(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
        response.write(response_cached())
        return response


all_urls = [
    url('', RequestHtml, name='home'),
    url('1kb-response', Request1kb, name='1kbresponse'),
    url('100kb-response', Request100kb, name='100kbresponse'),
    url('1mb-response', Request1mb, name='1mbresponse'),
    url('json-response', RequestJson, name='jsonresponse'),
    url('html-response', RequestHtml, name='htmlresponse'),
    url('slow-response', RequestSlow, name='slowresponse'),
    url('db-read', RequestDBread, name='dbread'),
    url('db-write', RequestDBwrite, name='dbwrite'),
    url('/cache-read', RequestCacheRead, name='cacheread'),
]

options = {}
app = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options=options
)
