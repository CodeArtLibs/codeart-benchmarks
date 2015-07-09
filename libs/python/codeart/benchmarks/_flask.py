from flask import Flask, request, Response, render_template, make_response, jsonify

from codeart.benchmarks import *


app = Flask(__name__)


def version():
    return flask.__version__


@app.route('/')
def request_home()():
    return response_html()

@app.route('/1kb-response')
def request_1kb():
    return Response(response_1kb(), content_type=CONTENT_TYPE_PLAIN)

@app.route('/100kb-response')
def request_100kb():
    return Response(response_100kb(), content_type=CONTENT_TYPE_PLAIN)

@app.route('/1mb-response')
def request_1mb():
    return Response(response_1mb(), content_type=CONTENT_TYPE_PLAIN)

@app.route('/json-response')
def request_json():
    return Response(response_json(), content_type=CONTENT_TYPE_JSON)

@app.route('/html-response')
def request_html():
    return Response(response_html(), content_type=CONTENT_TYPE_HTML)

@app.route('/slow-response')
def request_slow():
    return Response(response_slow(), content_type=CONTENT_TYPE_PLAIN)


@app.route('/db-read')
def request_db_read():
    return Response(response_db_read_queries(), content_type=CONTENT_TYPE_JSON)

@app.route('/db-write')
def request_db_write():
    return Response(response_db_write_queries(), content_type=CONTENT_TYPE_JSON)
