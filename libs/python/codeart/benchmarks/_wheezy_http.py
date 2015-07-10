import wheezy.http
from wheezy.http import HTTPResponse, WSGIApplication, bootstrap_http_defaults, not_found

from codeart.benchmarks import *


def version():
    return wheezy.http.__version__


def request_1kb(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
    response.write(response_1kb())
    return response

def request_100kb(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
    response.write(response_100kb())
    return response

def request_1mb(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
    response.write(response_1mb())
    return response

def request_json(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_JSON)]
    response.write(response_json())
    return response

def request_html(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_HTML)]
    response.write(response_html())
    return response

def request_slow(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
    response.write(response_slow())
    return response


def request_db_read(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_JSON)]
    response.write(response_db_read_queries())
    return response

def request_db_write(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_JSON)]
    response.write(response_db_write_queries())
    return response


def request_cache_read(request):
    response = HTTPResponse()
    response.headers = [(CONTENT_TYPE, CONTENT_TYPE_PLAIN)]
    response.write(response_cached())
    return response



def router_middleware(request, following):
    path = request.path
    if path == '/':
        response = request_html(request)
    elif path == '/1kb-response':
        response = request_1kb(request)
    elif path == '/100kb-response':
        response = request_100kb(request)
    elif path == '/1mb-response':
        response = request_1mb(request)
    elif path == '/json-response':
        response = request_json(request)
    elif path == '/html-response':
        response = request_html(request)
    elif path == '/slow-response':
        response = request_slow(request)
    elif path == '/db-read':
        response = request_db_read(request)
    elif path == '/db-write':
        response = request_db_write(request)
    elif path == '/cache-read':
        response = request_cache_read(request)
    else:
        response = not_found()
    return response

options = {}
app = WSGIApplication([bootstrap_http_defaults, lambda ignore: router_middleware], options)

