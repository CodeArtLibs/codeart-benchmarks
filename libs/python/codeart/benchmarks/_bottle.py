import bottle
from bottle import route, response

from codeart.benchmarks import *


def version():
    return bottle.__version__


@route('/')
def request_home():
    return request_html()

@route('/1kb-response')
def request_1kb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response_1kb()

@route('/100kb-response')
def request_100kb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response_100kb()

@route('/1mb-response')
def request_1mb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response_1mb()

@route('/json-response')
def request_json():
    response.content_type = CONTENT_TYPE_JSON
    return response_json()

@route('/html-response')
def request_html():
    response.content_type = CONTENT_TYPE_HTML
    return response_html()

@route('/slow-response')
def request_slow():
    response.content_type = CONTENT_TYPE_PLAIN
    return response_slow()


@route('/db-read')
def request_db_read_queries():
    response.content_type = CONTENT_TYPE_JSON
    return response_db_read_queries()

@route('/db-write')
def request_db_write_queries():
    response.content_type = CONTENT_TYPE_JSON
    return response_db_write_queries()


@route('/cache-read')
def request_cache_read():
    response.content_type = CONTENT_TYPE_PLAIN
    return response_cached()


app = bottle.default_app()
