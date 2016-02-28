# schemas.py
from mongothon import Schema

feature_request_schema = Schema({
    'title': {'type': basestring, 'required': True},
    'description': {'type': basestring, 'required': True},
    'client': {'type': basestring, 'required': True}, # String for now, eventually will be own Schema in future sprint
    'client_priority': {'type': basestring, 'required': True},
    'target_date': {'type': basestring, 'required': True},
    'ticket_url': {'type': basestring, 'required': True},
    'product_area': {'type': basestring, 'required': True},
    'agent': {'type': basestring, 'required': True}, # String for now, eventually will be own Schema in future sprint
    'created_at': {'type': basestring, 'required': True},
    'modified_at': {'type': basestring, 'required': True},
    'status': {'type': basestring, 'required': True},
})
