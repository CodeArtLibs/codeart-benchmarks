import mongoengine
import motorengine


class MongoEngineDoc(mongoengine.Document):
    field1 = mongoengine.StringField(max_length=200)
    field2 = mongoengine.StringField(max_length=200)
    field3 = mongoengine.StringField(max_length=200)


class MotorEngineDoc(motorengine.Document):
    field1 = motorengine.StringField(max_length=200)
    field2 = motorengine.StringField(max_length=200)
    field3 = motorengine.StringField(max_length=200)


def mongoengine_version():
    return mongoengine.__version__

def motorengine_version():
    return motorengine.__version__
