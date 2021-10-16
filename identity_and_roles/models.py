from typing_extensions import Required
from mongoengine import Document, fields
from mongoengine.queryset.base import CASCADE

class User(Document):
    first_name = fields.StringField(required=True)
    middle_name = fields.StringField()
    last_name = fields.StringField(required=True)
    
    email = fields.EmailField(required=True, unique=True)
    password = fields.StringField(required=True)

class Client(Document):
    key = fields.StringField(required=True)
    secret = fields.StringField(required=True)
    public_key = fields.StringField(required=True)
    user = fields.ReferenceField(User, reverse_delete_rule=CASCADE)
    realms = fields.StringField(required=True)
    default_realms = fields.StringField(required=True)
    redirect_uris = fields.StringField(required=True)
    default_redirect_uris = fields.StringField(required=True)