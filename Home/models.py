# Create your models here.

from mongoengine import *


class Contact(Document):
    name = StringField(max_length=122)
    country = StringField()
    email = StringField(max_length=122)
    phone = StringField(max_length=12)
    desc = StringField()

    def __str__(self):
        return self.name
