import wheezy.http
from wheezy.http import HTTPResponse, WSGIApplication, bootstrap_http_defaults, not_found

from codeart.benchmarks import *


def version():
    return wheezy.http.__version__


def request1kb(request):
    response = HTTPResponse()
    response.headers = [('Content-Type', CONTENT_TYPE_PLAIN)]
    response.write(response1kb())
    return response

def request100kb(request):
    response = HTTPResponse()
    response.headers = [('Content-Type', CONTENT_TYPE_PLAIN)]
    response.write(response100kb())
    return response

def request1mb(request):
    response = HTTPResponse()
    response.headers = [('Content-Type', CONTENT_TYPE_PLAIN)]
    response.write(response1mb())
    return response

def requestJson(request):
    response = HTTPResponse()
    response.headers = [('Content-Type', CONTENT_TYPE_JSON)]
    response.write(responseJson())
    return response

def requestHtml(request):
    response = HTTPResponse()
    response.headers = [('Content-Type', CONTENT_TYPE_HTML)]
    response.write(responseHtml())
    return response

def requestSlow(request):
    response = HTTPResponse()
    response.headers = [('Content-Type', CONTENT_TYPE_PLAIN)]
    response.write(responseSlow())
    return response


def requestDBcreate(request):
    pass
    # return mongoengine_create()
    # return motorengine_create()

def requestDBread(request):
    pass
    # return mongoengine_read()
    # return motorengine_read()

def requestDBcrud(request):
    pass
    # return mongoengine_crud()
    # return motorengine_crud()


def router_middleware(request, following):
    path = request.path
    if path == "/":
        response = requestHtml(request)
    elif path == "/1kb-response":
        response = request1kb(request)
    elif path == "/100kb-response":
        response = request100kb(request)
    elif path == "/1mb-response":
        response = request1mb(request)
    elif path == "/json-response":
        response = requestJson(request)
    elif path == "/html-response":
        response = requestHtml(request)
    elif path == "/slow-response":
        response = requestSlow(request)
    elif path == "/db-create":
        response = requestDBcreate(request)
    elif path == "/db-read":
        response = requestDBread(request)
    elif path == "/db-crud":
        response = requestDBcrud(request)
    else:
        response = not_found()
    return response

options = {}
app = WSGIApplication([bootstrap_http_defaults, lambda ignore: router_middleware], options)

