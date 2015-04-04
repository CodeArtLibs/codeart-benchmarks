import wheezy.http
from wheezy.http import HTTPResponse, WSGIApplication, bootstrap_http_defaults, not_found

from codeart.benchmarks import *


def version():
    return wheezy.http.__version__


def request1kb():
    response = HTTPResponse()
    response.write(response1kb())
    return response

def request100kb():
    response = HTTPResponse()
    response.write(response100kb())
    return response

def request1mb():
    response = HTTPResponse()
    response.write(response1mb())
    return response

def request1s():
    response = HTTPResponse()
    response.write(responseSleep1s())
    return response

def requestJson():
    response = HTTPResponse()
    response.write(responseJson())
    return response

def requestHtml():
    response = HTTPResponse()
    response.write(responseHtml())
    return response


def requestDBcreate():
    pass
    # return mongoengine_create()
    # return motorengine_create()

def requestDBread():
    pass
    # return mongoengine_read()
    # return motorengine_read()

def requestDBcrud():
    pass
    # return mongoengine_crud()
    # return motorengine_crud()


def router_middleware(request, following):
    path = request.path
    if path == "/1kb-response":
        response = request1kb(request)
    elif path == "/100kb-response":
        response = request100kb(request)
    elif path == "/1mb-response":
        response = request1mb(request)
    elif path == "/1s-response":
        response = request1s(request)
    elif path == "/json-response":
        response = requestJson(request)
    elif path == "/html-response":
        response = requestHtml(request)
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

