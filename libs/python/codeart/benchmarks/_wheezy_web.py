from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory

from codeart.benchmarks import *


class Request1kb(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(response1kb())
        return response

class Request100kb(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(response100kb())
        return response

class Request1mb(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(response1mb())
        return response

class Request1s(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(responseSleep1s())
        return response

class RequestJson(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(responseJson())
        return response

class RequestHtml(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(responseHtml())
        return response


class RequestDBcreate(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(OK)
        return response

class RequestDBread(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(OK)
        return response

class RequestDBcrud(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(OK)
        return response


all_urls = [
    url('', RequestHtml, name='home'),
    url(r"/1kb-response", Request1kb, name='1kbresponse'),
    url(r"/100kb-response", Request100kb, name='100kbresponse'),
    url(r"/1mb-response", Request1mb, name='1mbresponse'),
    url(r"/1s-response", Request1s, name='1sresponse'),
    url(r"/json-response", RequestJson, name='jsonresponse'),
    url(r"/html-response", RequestHtml, name='htmlresponse'),
    url(r"/db-create", RequestDBcreate, name='dbcreate'),
    url(r"/db-read", RequestDBread, name='dbread'),
    url(r"/db-crud", RequestDBcrud, name='dbcrud'),
]

options = {}
app = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options=options
)
