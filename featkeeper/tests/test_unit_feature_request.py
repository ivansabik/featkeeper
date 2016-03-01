# test_unit_feature.py
import sys
sys.path.append('/home/enivanrodrig/Desktop/featkeeper')
from featkeeper import schemas
import unittest
from pymongo import MongoClient
from featkeeper.models import FeatureRequest
from bson import ObjectId

class FeatureRequestUnitTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client.featkeeper_test
        self.collection = self.db.feature_requests
        self._populate_test_feature_requests()

    # Delete test db
    def tearDown(self):
        self.client.drop_database('featkeeper_test')

    def test_find_feature_requests(self):
        expected = [
            {
                '_id': '56d3d524402e5f1cfc273340',
                'title': 'Support custom themes',
                'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
                'client_name': 'Mandel Jamesdottir',
                'client_priority': 1,
                'target_date': '2016-08-21',
                'ticket_url': 'http://localhost:5000/LhPnCk',
                'product_area': 'Policies',
                'agent_name': 'Eleuthere',
                'created_at': '2016-02-28 23:35:19',
                'is_open': 1
            },
            {
                '_id': '56d3d524402e5f1cfc273344',
                'title': 'Support Google account auth',
                'description': 'Client wants to be able to login using Google accounts restricted to users in corporate domain',
                'client_name': 'Carlo Fibonacci',
                'client_priority': 2,
                'target_date': '2016-06-15',
                'ticket_url': 'http://localhost:5000/8VZuWu',
                'product_area': 'Billing',
                'agent_name': 'Eleonor',
                'created_at': '2015-12-20 09:15:20',
                'is_open': 1
            }
        ]
        feature_request = FeatureRequest()
        feature_requests = feature_request.find_all()
        self.assertEqual(expected, feature_requests)

    def test_find_feature_request_by_id(self):
        expected = {
            '_id': '56d3d524402e5f1cfc273340',
            'title': 'Support custom themes',
            'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
            'client_name': 'Mandel Jamesdottir',
            'client_priority': 1,
            'target_date': '2016-08-21',
            'ticket_url': 'http://localhost:5000/LhPnCk',
            'product_area': 'Policies',
            'agent_name': 'Eleuthere',
            'created_at': '2016-02-28 23:35:19',
            'is_open': 1
        }
        feature_request = FeatureRequest()
        feature_request = feature_request.find_by_id('56d3d524402e5f1cfc273340')
        self.assertEqual(expected, feature_request)

    def test_test_create_feature_request(self):
        self.fail('test_test_create_feature_request Not finished')

    def test_update_feature_request(self):
        self.fail('test_update_feature_request Not finished')

    def test_set_ticket_url(self):
        self.fail('test_set_ticket_url Not finished')

    '''
    A numbered priority according to the client (1...n).
    Client Priority numbers should not repeat for the given client,
    so if a priority is set on a new feature as "1",
    then all other feature requests for that client should be reordered.
    '''
    def test_reassign_new_feature_request_client_priority(self):
        self.fail('test_edit_feature Not finished')

    # Setup test data
    def _populate_test_feature_requests(self):
        feature_request = FeatureRequest()
        FeatureRequestModel = feature_request.FeatureRequestModel
        feature_request_1 = FeatureRequestModel({
            '_id': ObjectId('56d3d524402e5f1cfc273340'),
            'title': 'Support custom themes',
            'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
            'client_name': 'Mandel Jamesdottir',
            'client_priority': 1,
            'target_date': '2016-08-21',
            'ticket_url': 'http://localhost:5000/8VZuWu',
            'product_area': 'Policies',
            'agent_name': 'Eleuthere',
            'created_at': '2016-02-28 23:35:19',
            'is_open': 1
        })
        feature_request_1.save()
        feature_request_2 = FeatureRequestModel({
            '_id': ObjectId('56d3d524402e5f1cfc273342'),
            'title': 'Support Google account auth',
            'description': 'Client wants to be able to login using Google accounts restricted to users in corporate domain',
            'client_name': 'Carlo Fibonacci',
            'client_priority': 2,
            'target_date': '2016-06-15',
            'ticket_url': 'http://localhost:5000/8VZuWu',
            'product_area': 'Billing',
            'agent_name': 'Eleonor',
            'created_at': '2015-12-20 09:15:20',
            'is_open': 1
        })
        feature_request_2.save()

if __name__ == '__main__':
    unittest.main()
