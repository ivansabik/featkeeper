# schemas.py
from mongothon import *
from datetime import datetime

def feature_request_schema():
    return Schema({
        'title': {'type': basestring, 'required': True},
        'description': {'type': basestring, 'required': True},
        # String for now, eventually will be own Schema in future sprint
        'client_name': {'type': basestring, 'required': True},
        'client_priority': {'type': int, 'required': True, 'default': 1},
        'target_date': {'type': basestring, 'required': True},
        'ticket_url': {'type': basestring, 'required': True},
        'product_area': {'type': basestring, 'required': True},
        # String for now, eventually will be own Schema in future sprint
        'agent_name': {'type': basestring, 'required': True},
        'created_at': {'type': basestring, 'required': True, 'default': datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
        'modified_at': {'type': basestring},
        'is_open': {'type': int, 'required': True, 'default': 1}
    })
