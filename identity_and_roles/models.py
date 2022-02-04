from typing_extensions import Required
from mongoengine import Document, fields
from mongoengine.queryset.base import CASCADE

class User(Document):
    first_name = fields.StringField(required=True)
    middle_name = fields.StringField()
    last_name = fields.StringField(required=True)
    
    email = fields.EmailField(required=True, unique=True)
    password = fields.StringField(required=True)

GRANT_TYPE_CHOICES = [('authorization_code', 'Authorization code')]
RESPONSE_TYPE_CHOICES = [('code', 'Authorization code')]

class Client(Document):
    user = fields.ReferenceField(User)
    grant_type = fields.StringField(max_length=128, choices=GRANT_TYPE_CHOICES)
    response_type = fields.StringField(max_length=128, choices=RESPONSE_TYPE_CHOICES)
    scopes = fields.StringField()
    default_scopes = fields.StringField()
    redirect_uris = fields.StringField(required=True)
    default_redirect_uris = fields.StringField(required=True)

class BearerToken(Document):
    client = fields.ReferenceField(Client)
    user = fields.ReferenceField(User)
    scopes = fields.StringField()
    access_token = fields.StringField()
    refresh_token = fields.StringField()
    expires_at = fields.DateTimeField()

class AuthorizationCode(Document):
    client = fields.ReferenceField(Client)
    user = fields.ReferenceField(User)
    scopes = fields.StringField()
    redirect_uri = fields.StringField()
    code = fields.StringField()
    expiration_time = fields.DateTimeField()
    challenge = fields.StringField()
    challenge_method = fields.StringField()




