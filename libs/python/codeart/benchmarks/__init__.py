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
