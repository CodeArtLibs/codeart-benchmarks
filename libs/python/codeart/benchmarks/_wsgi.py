from codeart.benchmarks import *


def version():
    return 'spec'


def request_1kb(environ, start_response):
    data = RESPONSE_1KB
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_PLAIN),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]

def request_100kb(environ, start_response):
    data = RESPONSE_100KB
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_PLAIN),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]

def request_1mb(environ, start_response):
    data = RESPONSE_1MB
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_PLAIN),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]

def request_json(environ, start_response):
    response = RESPONSE_JSON
    data = to_json(response)
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_JSON),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]

def request_html(environ, start_response):
    data = RESPONSE_HTML
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_HTML),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]

def request_slow(environ, start_response):
    data = response_slow()
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_PLAIN),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]


def request_db_read(environ, start_response):
    data = response_db_read_queries()
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_JSON),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]

def request_db_write(environ, start_response):
    data = response_db_write_queries()
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_JSON),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]


def request_cache_read(environ, start_response):
    data = response_cached()
    response_headers = [
        (CONTENT_TYPE, CONTENT_TYPE_PLAIN),
        (CONTENT_LENGTH, str(len(data))),
    ]
    start_response(b'200 OK', response_headers)
    return [data]



def app(environ, start_response):
    path = environ['PATH_INFO']
    if path.startswith('/json-response'):
        return request_json(environ, start_response)
    elif path.startswith('/1kb-response'):
        return request_1kb(environ, start_response)
    elif path.startswith('/100kb-response'):
        return request_100kb(environ, start_response)
    elif path.startswith('/1mb-response'):
        return request_1mb(environ, start_response)
    elif path.startswith('/slow-response'):
        return request_slow(environ, start_response)
    elif path.startswith('/db-read'):
        return request_db_read(environ, start_response)
    elif path.startswith('/db-write'):
        return request_db_write(environ, start_response)
    elif path.startswith('/cache-read'):
        return request_cache_read(environ, start_response)
    else:
        return request_html(environ, start_response)
