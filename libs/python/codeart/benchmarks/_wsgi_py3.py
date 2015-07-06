from codeart.benchmarks import *


def response_1kb(environ, start_response):
    data = RESPONSE_1KB
    response_headers = [
        ('Content-type', CONTENT_TYPE_PLAIN),
        ('Content-Length', str(len(data))),
    ]
    start_response('200 OK', response_headers)
    return [bytes(data, 'utf-8')]

def response_100kb(environ, start_response):
    data = RESPONSE_100KB
    response_headers = [
        ('Content-type', CONTENT_TYPE_PLAIN),
        ('Content-Length', str(len(data))),
    ]
    start_response('200 OK', response_headers)
    return [bytes(data, 'utf-8')]

def response_1mb(environ, start_response):
    data = RESPONSE_1MB
    response_headers = [
        ('Content-type', CONTENT_TYPE_PLAIN),
        ('Content-Length', str(len(data))),
    ]
    start_response('200 OK', response_headers)
    return [bytes(data, 'utf-8')]

def response_json(environ, start_response):
    response = RESPONSE_JSON
    data = to_json(response)
    response_headers = [
        ('Content-type', CONTENT_TYPE_JSON),
        ('Content-Length', str(len(data))),
    ]
    start_response('200 OK', response_headers)
    return [bytes(data, 'utf-8')]

def response_html(environ, start_response):
    data = RESPONSE_HTML
    response_headers = [
        ('Content-type', CONTENT_TYPE_HTML),
        ('Content-Length', str(len(data))),
    ]
    start_response('200 OK', response_headers)
    return [bytes(data, 'utf-8')]

def response_slow(environ, start_response):
    data = responseSlow()
    response_headers = [
        ('Content-type', CONTENT_TYPE_PLAIN),
        ('Content-Length', str(len(data))),
    ]
    start_response('200 OK', response_headers)
    return [bytes(data, 'utf-8')]


def app(environ, start_response):
    path = environ['PATH_INFO']
    if path.startswith('/json-response'):
        return response_json(environ, start_response)
    elif path.startswith('/1kb-response'):
        return response_1kb(environ, start_response)
    elif path.startswith('/100kb-response'):
        return response_100kb(environ, start_response)
    elif path.startswith('/1mb-response'):
        return response_1mb(environ, start_response)
    elif path.startswith('/slow-response'):
        return response_slow(environ, start_response)
    else:
        return response_html(environ, start_response)
