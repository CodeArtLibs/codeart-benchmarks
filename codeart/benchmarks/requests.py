import json
import time

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json

from .models import MongoEngineDoc, MongoEngineDoc

# "/1kb-response"
# "/100kb-response"
# "/1mb-response"
# "/1s-response"
# "/json-response"
# "/html-response"
# "/db-create"
# "/db-read"
# "/db-crud"


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
RESPONSE_1S = lambda: time.sleep(1) # seconds
RESPONSE_1S_MSG = '1s response'
RESPONSE_HTML = '''
<ul>
    <li><a href="/1kb-response">1kb text</a></li>
    <li><a href="/100kb-response">100kb text</a></li>
    <li><a href="/1mb-response">1mb text</a></li>
    <li><a href="/1s-response">1s waiting</a></li>
    <li><a href="/json-response">JSON response</a></li>
    <li><a href="/html-response">HTML response</a></li>
    <li><a href="/db-create">MongoDB create</a></li>
    <li><a href="/db-read">MongoDB create</a></li>
    <li><a href="/db-crud">MongoDB list</a></li>
</ul>
'''

CONTENT_TYPE_PLAIN = 'text/plain'
CONTENT_TYPE_HTML = 'text/html; charset=utf-8'
CONTENT_TYPE_JSON = 'application/json'

def to_json(data):
    return json.dumps(data)


def response1kb():
    return RESPONSE_1KB

def response100kb():
    return RESPONSE_100KB

def response1mb():
    return RESPONSE_1MB

def response1s():
    return RESPONSE_1S

def responseJson():
    return to_json(RESPONSE_JSON)

def responseHtml():
    return RESPONSE_HTML

def responseSleep1s():
    time.sleep(1)
    return RESPONSE_1S_MSG


def mongoengine_create():
    MongoEngineDoc.objects.create(field1='1'*1, field2='2'*10, field3='3'*100)
    return OK

def mongoengine_read():
    MongoEngineDoc
    return OK

def mongoengine_crud():
    o, _ = MongoEngineDoc.objects.create(field1='1'*1, field2='2'*10, field3='3'*100)
    o = MongoEngineDoc.objects.filter(field1='1')[0]
    o.field1 = '11'
    o.save()
    o = MongoEngineDoc.objects.filter(field1='1')[0]
    o.delete()
    return OK


def motorengine_create():
    MotorEngineDoc.objects.create(field1='1'*1, field2='2'*10, field3='3'*100)
    return OK

def motorengine_read():
    MotorEngineDoc
    return OK

def motorengine_crud():
    def callback1():
        pass
    o, _ = MotorEngineDoc.objects.create(field1='1'*1, field2='2'*10, field3='3'*100, callback=callback1)
    def callback2():
        pass
    o = MotorEngineDoc.objects.filter(field1='1').find_all(callback2)
    o.field1 = '11'
    o.save()
    def callback3():
        pass
    o = MotorEngineDoc.objects.filter(field1='1').find_all(callback3)
    o.delete()
    return OK

def version():
    pass
