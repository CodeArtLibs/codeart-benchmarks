import os
from .responses import *


try:
    from mongoengine import connect
    connect('default')
    print('[MongoEngine] Connecting to DEV MongoDB')
except Exception as e:
    print('[MongoEngine] Unable to connect to MongoDB server')
    print(str(e))

try:
    from motorengine import connect
    connect('default')
    print('[MotorEngine] Connecting to DEV MongoDB')
except Exception as e:
    print('[MotorEngine] Unable to connect to MongoDB server')
    print(str(e))


recreate_db = os.getenv('RECREATE_DB', 'False').strip().lower()
if recreate_db in ('true', 'yes', '1'):
    from .models import create_test_db
    create_test_db()
