'''
models.py
Implements FeatureRequest including method for reassigning client priority
CRUD methods ORM style
'''

from mongothon import *
from datetime import datetime
from pymongo import MongoClient
import shortuuid

class FeatureRequest:
    is_open = 1

    def __init__(self,test=False):
        self.client = MongoClient()
        self.db = self.client.featkeeper
        if test==True:
            self.db = self.client.featkeeper_test
        self.collection = self.db.feature_requests
        self.FeatureRequestModel = create_model(self.feature_request_schema(), self.collection)

    def save(self):
        if not hasattr(self, 'created_at'):
            self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not hasattr(self, 'ticket_url'):
            self.ticket_url = 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
        # Persist to db
        FeatureRequestModel = self.FeatureRequestModel
        # If self._id exists it should update existing feature request, else not create new feature request
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

    def find_all(self):
        feature_requests = self.FeatureRequestModel.find()
        feature_requests_list = []
        for feature_request_model in feature_requests:
            feature_request = FeatureRequest(test=True)
            feature_requests_list.append(self._decode_feature_request(feature_request, feature_request_model))
        return feature_requests_list

    def find_by_id(self, feature_request_id):
        feature_request = self.FeatureRequestModel.find_by_id(feature_request_id)
        return self._decode_feature_request(self, feature_request)

    @classmethod
    def feature_request_schema(cls):
        return Schema({
            'title': {'type': basestring, 'required': True},
            'description': {'type': basestring, 'required': True},
            # String for now, eventually will be own Schema
            'client_name': {'type': basestring, 'required': True},
            'client_priority': {'type': int, 'required': True},
            'target_date': {'type': basestring, 'required': True},
            # Currently ticket URL is generated, later a custom input filed can be added to track visits to that URL coming from the app (as goo.gl, bit.ly, etc)
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
        feature_requests_dict['title']  = self.title
        feature_requests_dict['description']  = self.description
        feature_requests_dict['client_name']  = self.client_name
        feature_requests_dict['client_priority']  = self.client_priority
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
        feature_request_object.description = feature_request_dict['description']
        feature_request_object.client_name = feature_request_dict['client_name']
        feature_request_object.client_priority = feature_request_dict['client_priority']
        feature_request_object.target_date = feature_request_dict['target_date']
        feature_request_object.ticket_url = feature_request_dict['ticket_url']
        feature_request_object.product_area = feature_request_dict['product_area']
        feature_request_object.agent_name = feature_request_dict['agent_name']
        feature_request_object.created_at = feature_request_dict['created_at']
        feature_request_object.is_open = feature_request_dict['is_open']
        # Modified at is optional, if document not edited will no be set, assign separately
        try:
            feature_request_object.modified_at = feature_request_dict['modified_at']
        except KeyError:
            pass
        return feature_request_object

    # From: http://stackoverflow.com/questions/14813396/python-elegant-way-to-delete-empty-lists-from-python-dict
    def _remove_empty_keys(self, d):
        for k in d.keys():
            if not d[k]:
                del d[k]
        return d

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self._remove_empty_keys(self.__dict__) == self._remove_empty_keys(other.__dict__))

    def __ne__(self, other):
        return not self.__eq__(other)
