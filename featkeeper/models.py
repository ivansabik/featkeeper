'''
models.py
Implements User and FeatureRequest
CRUD methods ODM style based on schema and defining custom
save, find_by_id, find_all public methods

Username and hash should not be used in API! not included in to_dict, declared as private
Exposes public static auth method, no need to access directly username and hash

Toekn based auth implementation based on sample by Miguel Grinberg
http://blog.miguelgrinberg.com/post/restful-authentication-with-flask
'''

from mongothon import *
from datetime import datetime
from pymongo import MongoClient
import shortuuid
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from werkzeug.security import generate_password_hash, check_password_hash

# User class
class User:
    type = 'agent'
    access_is_enabled = 1

    def __init__(self, test=False):
        self._hashim = None
        self.client = MongoClient()
        self.db = self.client.featkeeper
        if test == True:
            self.db = self.client.featkeeper_test
        self.test = test
        self.collection = self.db.users
        self.UserModel = create_model(
            self.user_schema(), self.collection
        )

    # Using encrypted tokens with expiration time
    @classmethod
    def auth(cls, username, password):
        pass

    # http://flask.pocoo.org/snippets/54/
    def set_password(self, password):
        self.hashim = generate_password_hash(password)

    # http://flask.pocoo.org/snippets/54/
    def verify_password(self, password):
        return check_password_hash(self._hashim, password)

    # http://flask.pocoo.org/snippets/54/
    def verify_password(self, password):
        return check_password_hash(self._hashim, password)

    def get_token(self):
        if self.test:
            secret_key = 'NOT_SO_SECRET_KEY'
        else:
            secret_key = '' # Get from config!
        s = Serializer(secret_key, expires_in = 30)
        return s.dumps({'username': self.username, 'type': self.type })

    @classmethod
    def verify_token(cls, token):
        s = Serializer('NOT_SO_SECRET_KEY')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return False
        except BadSignature:
            return False
        return True # In near future will be a dict response of the auth user

    def find_all(self, user_type='agent'):
        pass

    def find_by_username(self, username):
        user = self.UserModel.find_one({'username': username})
        return self._decode_user(self, user)

    def _decode_user(self, user_object, user_dict):
        user_object._id = str(user_dict['_id'])
        user_object.username = user_dict['username']
        user_object.hashim = user_dict['hashim']
        user_object.type = user_dict['type']
        user_object.created_at = user_dict['created_at']
        user_object.access_is_enabled = user_dict['access_is_enabled']
        # Modified at is optional, if document not edited will no be set, assign separately
        try:
            user_object.modified_at = user_dict['modified_at']
        except KeyError:
            pass

        return user_object

    def save(self):
        pass

    @classmethod
    def user_schema(cls):
        return Schema({
            'username': {'type': basestring, 'required': True},
            'hashim': {'type': basestring, 'required': True},
            'type': {'type': basestring, 'required': True,  'default': 'agent'},
            'created_at': {'type': basestring, 'required': True, 'default': datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
            'modified_at': {'type': basestring},
            'access_is_enabled': {'type': int, 'required': True, 'default': 1}
        })

    def to_dict(self):
        user_dict = {}
        user_dict['_id'] = self._id
        user_dict['username'] = self.title
        user_dict['hashim'] = self.description
        user_dict['type'] = self.client_name
        user_dict['created_at'] = self.created_at
        user_dict['access_is_enabled'] = self.client_priority
        if hasattr(self, 'modified_at'):
            user_dict['modified_at'] = self.modified_at
        return user_dict

# FetureRequest class
class FeatureRequest:
    is_open = 1

    def __init__(self, test=False):
        self.client = MongoClient()
        self.db = self.client.featkeeper
        if test == True:
            self.db = self.client.featkeeper_test
        self.test = test
        self.collection = self.db.feature_requests
        self.FeatureRequestModel = create_model(
            self.feature_request_schema(), self.collection
        )

    def find_all(self):
        feature_requests = self.FeatureRequestModel.find()
        feature_requests_list = []
        for feature_request_model in feature_requests:
            feature_request = FeatureRequest(test=self.test)
            feature_requests_list.append(self._decode_feature_request(
                feature_request, feature_request_model))
        return feature_requests_list

    def find_by_id(self, feature_request_id):
        feature_request = self.FeatureRequestModel.find_by_id(
            feature_request_id)
        return self._decode_feature_request(self, feature_request)

    def save(self):
        if not hasattr(self, 'created_at'):
            self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not hasattr(self, 'ticket_url'):
            self.ticket_url = 'http://localhost:5000/' + \
                shortuuid.ShortUUID().random(length=6)
        # Persist to db
        FeatureRequestModel = self.FeatureRequestModel
        # If self._id exists it should update existing feature request, else create new feature request
        # Update existing feature request
        if hasattr(self, '_id'):
            feature_request = FeatureRequestModel.find_by_id(self._id)
            self.modified_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            feature_request['title'] = self.title
            # @todo only assing if exist!
            if hasattr(self, 'description'):
                feature_request['description'] = self.description
            if hasattr(self, 'client_name'):
                feature_request['client_name'] = self.client_name
            if hasattr(self, 'client_priority'):
                feature_request['client_priority'] = self.client_priority
            if hasattr(self, 'target_date'):
                feature_request['target_date'] = self.target_date
            if hasattr(self, 'product_area'):
                feature_request['product_area'] = self.product_area
            if hasattr(self, 'agent_name'):
                feature_request['agent_name'] = self.agent_name
            feature_request['modified_at'] = self.modified_at
            feature_request.save()
        # Create new existing feature request
        else:
            feature_request = FeatureRequestModel({
                'title': self.title,
                'description': self.description,
                'client_name': self.client_name,
                'client_priority': self.client_priority,
                'target_date': self.target_date,
                'product_area': self.product_area,
                'agent_name': self.agent_name,
                'ticket_url': self.ticket_url
            })
            feature_request.save()
            self._id = str(feature_request['_id'])
        # Return dict representation including id assigned from db
        self._reassign_client_priorities(feature_request)
        saved_feature_request = {
            '_id': self._id,
            'title': self.title,
            'description': self.description,
            'client_name': self.client_name,
            'client_priority': self.client_priority,
            'target_date': self.target_date,
            'created_at': self.created_at,
            'product_area': self.product_area,
            'agent_name': self.agent_name,
            'ticket_url': self.ticket_url
        }
        if hasattr(self, 'modified_at'):
            saved_feature_request['modified_at'] = self.modified_at
        return saved_feature_request

    def _reassign_client_priorities(self, feature_request_dict):
        # find others with same Client
        feature_requests_same_client = self.FeatureRequestModel.find(
            {
                '$and': [
                    {'_id': {'$ne': feature_request_dict['_id']}},
                    {'client_name': feature_request_dict['client_name']}
                ]
            }
        )
        for feature_request_model in feature_requests_same_client:
            self._reassign_client_priority(feature_request_model)

    def _reassign_client_priority(self, feature_request_dict):
        try:
            # find other feature request with same client sorted by priority
            feature_request_same_priority = self.FeatureRequestModel.find_one(
                {
                    '$and': [
                        {'_id': feature_request_dict['_id']},
                        {'client_name': feature_request_dict['client_name']},
                        {'client_priority': feature_request_dict[
                            'client_priority']}
                    ]
                }
            )
            feature_request_same_priority['client_priority'] += 1
            feature_request_same_priority.save()
        except:
            pass

    @classmethod
    def feature_request_schema(cls):
        return Schema({
            'title': {'type': basestring, 'required': True},
            'description': {'type': basestring, 'required': True},
            # String for now, eventually will be own Schema
            'client_name': {'type': basestring, 'required': True},
            'client_priority': {'type': int, 'required': True},
            'target_date': {'type': basestring, 'required': True},
            # Currently ticket URL is generated, later a custom input filed can
            # be added to track visits to that URL coming from the app (as
            # goo.gl, bit.ly, etc)
            'ticket_url': {'type': basestring, 'required': True, 'default': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)},
            'product_area': {'type': basestring, 'required': True},
            # String for now, eventually will be own Schema
            'agent_name': {'type': basestring, 'required': True},
            'created_at': {'type': basestring, 'required': True, 'default': datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
            'modified_at': {'type': basestring},
            'is_open': {'type': int, 'required': True, 'default': 1}
        })

    def to_dict(self):
        feature_requests_dict = {}
        feature_requests_dict['_id'] = self._id
        feature_requests_dict['title'] = self.title
        feature_requests_dict['description'] = self.description
        feature_requests_dict['client_name'] = self.client_name
        feature_requests_dict['client_priority'] = self.client_priority
        feature_requests_dict['target_date'] = self.target_date
        feature_requests_dict['ticket_url'] = self.ticket_url
        feature_requests_dict['product_area'] = self.product_area
        feature_requests_dict['agent_name'] = self.agent_name
        feature_requests_dict['created_at'] = self.created_at
        feature_requests_dict['is_open'] = self.is_open
        if hasattr(self, 'modified_at'):
            feature_requests_dict['modified_at'] = self.modified_at
        return feature_requests_dict

    def _decode_feature_request(self, feature_request_object, feature_request_dict):
        feature_request_object._id = str(feature_request_dict['_id'])
        feature_request_object.title = feature_request_dict['title']
        feature_request_object.description = feature_request_dict[
            'description']
        feature_request_object.client_name = feature_request_dict[
            'client_name']
        feature_request_object.client_priority = feature_request_dict[
            'client_priority']
        feature_request_object.target_date = feature_request_dict[
            'target_date']
        feature_request_object.ticket_url = feature_request_dict['ticket_url']
        feature_request_object.product_area = feature_request_dict[
            'product_area']
        feature_request_object.agent_name = feature_request_dict['agent_name']
        feature_request_object.created_at = feature_request_dict['created_at']
        feature_request_object.is_open = feature_request_dict['is_open']
        # Modified at is optional, if document not edited will no be set, assign separately
        try:
            feature_request_object.modified_at = feature_request_dict['modified_at']
        except KeyError:
            pass
        return feature_request_object

    # http://stackoverflow.com/questions/14813396/python-elegant-way-to-delete-empty-lists-from-python-dict
    def _remove_empty_keys(self, d):
        for k in d.keys():
            if not d[k]:
                del d[k]
        return d

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self._remove_empty_keys(self.__dict__) == self._remove_empty_keys(other.__dict__))

    def __ne__(self, other):
        return not self.__eq__(other)
