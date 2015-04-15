from flask import Flask, request, Response, render_template, make_response, jsonify

from codeart.benchmarks import *


app = Flask(__name__)


def version():
    return flask.__version__


@app.route('/')
def requestHome():
    return requestHtml()

@app.route('/1kb-response')
def request1kb():
    return Response(response1kb(), content_type=CONTENT_TYPE_PLAIN)

@app.route('/100kb-response')
def request100kb():
    return Response(response100kb(), content_type=CONTENT_TYPE_PLAIN)

@app.route('/1mb-response')
def request1mb():
    return Response(response1mb(), content_type=CONTENT_TYPE_PLAIN)

@app.route('/1s-response')
def request1s():
    return Response(responseSleep1s(), content_type=CONTENT_TYPE_PLAIN)

@app.route('/json-response')
def requestJson():
    return Response(responseJson(), content_type=CONTENT_TYPE_JSON)

@app.route('/html-response')
def requestHtml():
    return Response(responseHtml(), content_type=CONTENT_TYPE_HTML)


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
