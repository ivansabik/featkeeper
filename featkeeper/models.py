# models.py
from mongothon import *
from datetime import datetime
from pymongo import MongoClient

class FeatureRequest:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.featkeeper
        self.collection = self.db.feature_requests
        self.FeatureRequestModel = create_model(self.feature_request_schema(), self.collection)

    def find_all(self):
        feature_requests = self.FeatureRequestModel.find()
        return self._decode_feature_requests(feature_requests)

    def find_by_id(self, feature_request_id):
        feature_request = self.FeatureRequestModel.find_by_id(feature_request_id)
        return self._decode_feature_request(feature_request)

    @classmethod
    def feature_request_schema(cls):
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

    def _decode_feature_requests(self, feature_requests):
        return feature_requests

    def _decode_feature_request(self, feature_request):
        feature_request_dict = {
            '_id': str(feature_request['_id']),
            'title': feature_request['title'],
            'description': feature_request['description'],
            'client_name': feature_request['client_name'],
            'client_priority': feature_request['client_priority'],
            'target_date': feature_request['target_date'],
            'ticket_url': feature_request['ticket_url'],
            'product_area': feature_request['product_area'],
            'agent_name': feature_request['agent_name'],
            'created_at': feature_request['created_at'],
            'is_open': feature_request['is_open']
        }
        try:
            feature_request_dict['modified_at'] = feature_request['modified_at']
        except KeyError:
            pass
        return self._remove_empty_keys(feature_request)

    # http://stackoverflow.com/questions/14813396/python-elegant-way-to-delete-empty-lists-from-python-dict
    def _remove_empty_keys(self, d):
        for k in d.keys():
            if not d[k]:
                del d[k]
        return d

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)
