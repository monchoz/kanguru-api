from mongoengine import *

MONGO_DATABASE_NAME = 'kanguru'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
connect(MONGO_DATABASE_NAME, host=MONGO_HOST, port=MONGO_PORT)

class User(Document):
    name = StringField(max_length=50)
    username = StringField(max_length=30)
    email = EmailField(max_length=30)
