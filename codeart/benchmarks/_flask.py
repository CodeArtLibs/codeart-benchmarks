from flask import Flask, request, render_template, make_response, jsonify

from codeart.benchmarks import *


app = Flask(__name__)


def version():
    pass


@app.route('/1kb-response')
def request1kb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response1kb()

@app.route('/100kb-response')
def request100kb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response100kb()

@app.route('/1mb-response')
def request1mb():
    response.content_type = CONTENT_TYPE_PLAIN
    return response1mb()

@app.route('/1s-response')
def request1s():
    response.content_type = CONTENT_TYPE_PLAIN
    return responseSleep1s()

@app.route('/json-response')
def requestJson():
    response.content_type = CONTENT_TYPE_JSON
    return responseJson()

@app.route('/html-response')
def requestHtml():
    response.content_type = CONTENT_TYPE_HTML
    return responseHtml()


@app.route('/db-create')
def requestDBcreate():
    pass
    # return mongoengine_create()
    # return motorengine_create()

@app.route('/db-read')
def requestDBread():
    pass
    # return mongoengine_read()
    # return motorengine_read()

@app.route('/db-crud')
def requestDBcrud():
    pass
    # return mongoengine_crud()
    # return motorengine_crud()
