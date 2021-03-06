'''
test_unit_feature_request.py
Tests FeatureRequest behaviour (find, save, validation methods, etc)
@todo: Should validate feature request model
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import unittest
from featkeeper.models import FeatureRequest
from utils import FeatkeeperTestUtils

class FeatureRequestUnitTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        FeatkeeperTestUtils.populate_test_feature_requests()

    # Delete test db
    def tearDown(self):
        FeatkeeperTestUtils.destroy_test_db()

    # Test when instanced with default test parameter uses dev db
    def test_use_dev_db(self):
        feature_request = FeatureRequest()
        self.assertEqual('featkeeper', feature_request.db-name)

    # Test when instanced with test parameter actually uses test db
    def test_use_test_db(self):
        feature_request = FeatureRequest(test=True)
        self.assertEqual('featkeeper_test', feature_request.db-name)

    # Test find all feature requests
    def test_find_feature_requests(self):
        expected = [
            {
                '_id': '56d3d524402e5f1cfc273340',
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
            },
            {
                '_id': '56d3d524402e5f1cfc273342',
                'title': 'Support Google account auth',
                'description': 'Client wants to be able to login using Google accounts restricted to users in corporate domain',
                'client_name': 'Mandel Jamesdottir',
                'client_priority': 2,
                'target_date': '2016-06-15',
                'ticket_url': 'http://localhost:5000/LhPnCk',
                'product_area': 'Billing',
                'agent_name': 'Eleonor',
                'created_at': '2015-12-20 09:15:20',
                'is_open': 1
            }
        ]
        feature_request = FeatureRequest(test=True)
        feature_requests = feature_request.find_all()
        self.assertEqual(expected[0], feature_requests[0].to_dict())

    # Test find specific feature request by id
    def test_find_feature_request_by_id(self):
        expected = {
            '_id': '56d3d524402e5f1cfc273340',
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
        }
        feature_request = FeatureRequest(test=True)
        feature_request = feature_request.find_by_id(
            '56d3d524402e5f1cfc273340')
        self.assertEqual(expected, feature_request.to_dict())

    # Test create new feature request
    def test_create_feature_request(self):
        feature_request = FeatureRequest(test=True)
        feature_request.title = 'Add end to end encripted chat'
        feature_request.description = 'Client wants to be able to send P2P encrypted messages to customers in realtime'
        feature_request.client_name = 'Akbar Erickssohn'
        feature_request.client_priority = 1
        feature_request.target_date = '2016-10-29'
        feature_request.created_at = '2016-02-28 23:35:19'
        feature_request.product_area = 'Policies'
        feature_request.agent_name = 'Eleuthere'
        feature_request.ticket_url = 'http://localhost:5000/1a2eaD'
        expected = {
            'title': 'Add end to end encripted chat',
            'description': 'Client wants to be able to send P2P encrypted messages to customers in realtime',
            'client_name': 'Akbar Erickssohn',
            'client_priority': 1,
            'target_date': '2016-10-29',
            'product_area': 'Policies',
            'agent_name': 'Eleuthere'
        }
        # Remove _id for test assertions since its random, first check that
        # exists
        result = feature_request.save()
        self.assertIsNot(None, result['_id'])
        self.assertIsNot(None, result['created_at'])
        self.assertIsNot(None, result['ticket_url'])
        del result['_id']
        del result['created_at']
        del result['ticket_url']
        self.assertEqual(expected, result)

    # Test edit an existing feature request
    def test_update_feature_request(self):
        feature_request = FeatureRequest(test=True)
        feature_request = feature_request.find_by_id(
            '56d3d524402e5f1cfc273342')
        feature_request.product_area = 'Policies'
        result = feature_request.save()
        # Assign none to retrieve again and check new product area associated
        feature_request = FeatureRequest(test=True)
        feature_request = feature_request.find_by_id(
            '56d3d524402e5f1cfc273342')
        self.assertEqual(True, hasattr(feature_request, 'modified_at'))
        self.assertEqual('Policies', feature_request.product_area)

    # Test reassign client priority for all existing feature requests when
    # colliding with a new one
    def test_reassign_new_feature_request_client_priority(self):
        feature_request_1 = FeatureRequest(
            test=True).find_by_id('56d3d524402e5f1cfc273340')
        feature_request_2 = FeatureRequest(
            test=True).find_by_id('56d3d524402e5f1cfc273342')
        # Check priority before changing
        self.assertEqual(1, feature_request_1.client_priority)
        self.assertEqual(2, feature_request_2.client_priority)
        # Change priority and re-check new assignment
        feature_request_2.client_priority = 1
        feature_request_2.save()
        feature_request_1 = FeatureRequest(
            test=True).find_by_id('56d3d524402e5f1cfc273340')
        feature_request_2 = FeatureRequest(
            test=True).find_by_id('56d3d524402e5f1cfc273342')
        self.assertEqual(1, feature_request_2.client_priority)
        self.assertEqual(2, feature_request_1.client_priority)

if __name__ == '__main__':
    unittest.main()
