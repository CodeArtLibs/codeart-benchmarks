import os
import json
import random
import time

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json

try:
    # Py2
    range = xrange
except NameError:
    # Py3
    pass

from .models import *

# "/1kb-response"
# "/100kb-response"
# "/1mb-response"
# "/json-response"
# "/slow-response"
# "/html-response"
# "/db-read"
# "/db-write"


OK = 'OK'
CHARS10 = '1kb 1kb - '
RESPONSE_1KB = CHARS10 * 100 # ~1kb
RESPONSE_100KB = CHARS10 * 10000 # ~100kb
RESPONSE_1MB = CHARS10 * 100000 # ~1mb

RESPONSE_JSON = {
    'username': 'codeart',
    'permissions': ['create', 'update', 'list', 'read', 'delete'],
    'groups': {'group1': 'crlud', 'group2': 'cr', 'group3': 'crlu'},
}

RESPONSE_SLOW = float(os.getenv('N_SECONDS', 0.1)) # seconds
RESPONSE_SLOW_MSG = '{}s response'.format(RESPONSE_SLOW)

RESPONSE_HTML = '''
<ul>
    <li><a href="/1kb-response">1kb text</a></li>
    <li><a href="/100kb-response">100kb text</a></li>
    <li><a href="/1mb-response">1mb text</a></li>
    <li><a href="/json-response">JSON response</a></li>
    <li><a href="/html-response">HTML response</a></li>
    <li><a href="/slow-response">{}s waiting</a></li>

    <li><a href="/db-read">MongoDB select queries</a></li>
    <li><a href="/db-write">MongoDB write queries</a></li>
</ul>
'''.format(RESPONSE_SLOW, RESPONSE_SLOW)

CONNECTION_CLOSE = 'close'
CONNECTION_KEEP_ALIVE = 'keep-alive'
CONTENT_LENGTH = 'Content-Length'
CONTENT_TYPE = 'Content-Type'
CONTENT_TYPE_PLAIN = 'text/plain'
CONTENT_TYPE_HTML = 'text/html; charset=utf-8'
CONTENT_TYPE_JSON = 'application/json; charset=utf-8'


def to_json(data):
    return json.dumps(data)


def response_1kb():
    return RESPONSE_1KB

def response_100kb():
    return RESPONSE_100KB

def response_1mb():
    return RESPONSE_1MB

def response_json():
    return to_json(RESPONSE_JSON)

def response_html():
    return RESPONSE_HTML

def response_slow():
    time.sleep(RESPONSE_SLOW)
    return RESPONSE_SLOW_MSG


def response_db_read_queries():
    engine = os.getenv('DB_ENGINE', None)
    if engine == 'motorengine':
        r = motorengine_read_queries()
    else:
        r = mongoengine_read_queries()
    return to_json(r)

def response_db_write_queries():
    engine = os.getenv('DB_ENGINE', None)
    if engine == 'motorengine':
        r = motorengine_write_queries()
    else:
        r = mongoengine_write_queries()
    return to_json(r)


def mongoengine_read_queries():
    '''
    1 select count
    10 selects by index
    '''
    n = MongoEngineDoc.objects.count()
    r = []
    for _ in range(10):
        i = random.randint(0, n-1)
        o = MongoEngineDoc.objects.all()[i]
        r.append(o.to_json())
    return r

def mongoengine_write_queries():
    '''
    10 insert queries
    '''
    r = []
    for _ in range(10):
        v = os.urandom(24).encode('hex')
        o = MongoEngineDoc2.objects.create(field1=v, field2=v, field3=v, field4=v, field5=v)
        r.append(o.to_json())
    return r


def motorengine_read_queries():
    '''
    1 select count
    10 selects by index
    '''
    n = MotorEngineDoc.objects.count()
    r = []
    for _ in range(10):
        i = random.randint(0, n-1)
        o = MotorEngineDoc.objects.all()[i]
        r.append(o.to_json())
    return r

def motorengine_write_queries():
    '''
    10 insert queries
    '''
    r = []
    for _ in range(10):
        v = os.urandom(24).encode('hex')
        o = MotorEngineDoc2.objects.create(field1=v, field2=v, field3=v, field4=v, field5=v)
        r.append(o.to_json())
    return r
