from bottle import route, response

from codeart.benchmarks import *


@route('/1kb-response')
def request1kb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response1kb()


@route('/100kb-response')
def request100kb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response100kb()


@route('/1mb-response')
def request1mb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response1mb()


@route('/1s-response')
def request1s():
    response.content_type = CONTENT_TYPE_PLAIN
    return responseSleep1s()


@route('/json-response')
def requestJson():
    response.content_type = CONTENT_TYPE_JSON
    return responseJson()


@route('/html-response')
def requestHtml():
    response.content_type = CONTENT_TYPE_HTML
    return responseHtml()

@route('/db-create')
def requestDBcreate():
    pass
    # return mongoengine_create()
    # return motorengine_create()

@route('/db-read')
def requestDBread():
    pass
    # return mongoengine_read()
    # return motorengine_read()

@route('/db-crud')
def requestDBcrud():
    pass
    # return mongoengine_crud()
    # return motorengine_crud()


def versions():
    return dict(
        python=1,
        bottle=1,
        falcon=1,
        tornado=1,
        mongoengine=1,
        motorengine=1,
        ujson=1,
        simplejson=1,
    )
