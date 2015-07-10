import os
from .responses import *


try:
    from mongoengine import connect
    connect('default')
    print('[MongoEngine] Connected to DEV MongoDB')
    recreate_db = os.getenv('RECREATE_DB', 'False').strip().lower()
    if recreate_db in ('true', 'yes', '1'):
        from .models import create_mongoengine_test_db
        create_mongoengine_test_db()
except Exception as e:
    print('[MongoEngine] Unable to connect or populate MongoDB server')
    print(str(e))

try:
    from motorengine import connect
    connect('default')
    print('[MotorEngine] Connected to DEV MongoDB')
    recreate_db = os.getenv('RECREATE_DB', 'False').strip().lower()
    if recreate_db in ('true', 'yes', '1'):
        from .models import create_motorengine_test_db
        create_motorengine_test_db()
except Exception as e:
    print('[MotorEngine] Unable to connect or populate MongoDB server')
    print(str(e))


populate_cache()