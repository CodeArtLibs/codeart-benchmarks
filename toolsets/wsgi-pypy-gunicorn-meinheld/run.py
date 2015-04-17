# from codeart.benchmarks._wsgi import *
from codeart.benchmarks.requests import *


import logging
logging.disable(logging.CRITICAL)
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
logger.disabled = True
logger.propagate = False

def response_json(environ, start_response):
    response = RESPONSE_JSON
    data = to_json(response)
    response_headers = [
        ('Content-type', CONTENT_TYPE_JSON),
        ('Content-Length', str(len(data)))
    ]
    start_response(b'200 OK', response_headers)
    return [data]

def response_html(environ, start_response):
    data = RESPONSE_HTML
    response_headers = [
        ('Content-type', CONTENT_TYPE_HTML),
        ('Content-Length', str(len(data)))
    ]
    start_response(b'200 OK', response_headers)
    return [data]


def app(environ, start_response):
    path = environ['PATH_INFO']
    if path.startswith('/json-response'):
        return response_json(environ, start_response)
    else:
        return response_html(environ, start_response)
