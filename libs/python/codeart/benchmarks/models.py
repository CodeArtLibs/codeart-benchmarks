import os

import mongoengine
import motorengine


def mongoengine_version():
    return mongoengine.__version__

def motorengine_version():
    return motorengine.__version__


class MongoEngineDoc(mongoengine.Document):
    field1 = mongoengine.StringField(max_length=200)
    field2 = mongoengine.StringField(max_length=200)
    field3 = mongoengine.StringField(max_length=200)
    field4 = mongoengine.StringField(max_length=200)
    field5 = mongoengine.StringField(max_length=200)

class MongoEngineDoc2(mongoengine.Document):
    field1 = mongoengine.StringField(max_length=200)
    field2 = mongoengine.StringField(max_length=200)
    field3 = mongoengine.StringField(max_length=200)
    field4 = mongoengine.StringField(max_length=200)
    field5 = mongoengine.StringField(max_length=200)


class MotorEngineDoc(motorengine.Document):
    field1 = motorengine.StringField(max_length=200)
    field2 = motorengine.StringField(max_length=200)
    field3 = motorengine.StringField(max_length=200)
    field4 = motorengine.StringField(max_length=200)
    field5 = motorengine.StringField(max_length=200)

class MotorEngineDoc2(motorengine.Document):
    field1 = motorengine.StringField(max_length=200)
    field2 = motorengine.StringField(max_length=200)
    field3 = motorengine.StringField(max_length=200)
    field4 = motorengine.StringField(max_length=200)
    field5 = motorengine.StringField(max_length=200)


def create_test_db():
    MongoEngineDoc.objects.all().delete()
    MongoEngineDoc2.objects.all().delete()
    MotorEngineDoc.objects.all().delete()
    MotorEngineDoc2.objects.all().delete()
    for i in range(10000):
        v = os.urandom(24).encode('hex')
        MongoEngineDoc.objects.create(field1=v, field2=v, field3=v, field4=v, field5=v)
        MotorEngineDoc.objects.create(field1=v, field2=v, field3=v, field4=v, field5=v)
