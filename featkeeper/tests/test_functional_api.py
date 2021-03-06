'''
test_funcional_api.py
Tests API endpoints for CRUD operations
@todo: Should return erron when requesting feature request not found (view and edit)
@todo: Should return erron when trying to updated feature request without specifying _id
@todo: Should return warning when trying to create feature request with same content as existing one
@todo: Should validate feature request model
@todo: Should sort by created date
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from featkeeper import app
import unittest
from featkeeper.models import FeatureRequest, User
from flask import json
from utils import FeatkeeperTestUtils

API_ROOT_URL = '/api/v1'

class FeatkeeperApiTest(unittest.TestCase):
    maxDiff = 5000
    # Create client, db and collection for tests
    def setUp(self):
        app.test_mode = True
        self.app = app.app.test_client()
        FeatkeeperTestUtils.populate_test_feature_requests()
        FeatkeeperTestUtils.populate_test_users()

    # Delete test db
    def tearDown(self):
        pass#FeatkeeperTestUtils.destroy_test_db()

    # Test can start using test db
    def test_can_run_using_test_db(self):
        self.assertEqual(True, app.test_mode)

    # Test can serve static files (eventually will only be for dev or testing)
    def test_can_serve_static_file_app(self):
        javascript_response = self.app.get('/app.js')
        css_response = self.app.get('/app.css')
        self.assertEqual(200, javascript_response.status_code)
        self.assertEqual(200, css_response.status_code)

    # Test for GET /auth, should generate and return access token with
    # expiration for user with valid credentials and with login enabled
    # (access_is_disabled=0)
    def test_api_can_generate_and_return_token(self):
        self.fail('test_api_can_generate_and_return_token not finished!')

    # Test for GET /feature-request, should output get existing feature
    # requests
    def test_api_can_read_feature_requests(self):
        # Need to do fresh populate since other tests in suite are modifying test db
        FeatkeeperTestUtils.destroy_test_db()
        FeatkeeperTestUtils.populate_test_feature_requests()
        FeatkeeperTestUtils.populate_test_users()
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
                'client_name': 'Carlo Fibonacci',
                'client_priority': 2,
                'target_date': '2016-06-15',
                'ticket_url': 'http://localhost:5000/LhPnCk',
                'product_area': 'Billing',
                'agent_name': 'Eleonor',
                'created_at': '2015-12-20 09:15:20',
                'is_open': 1
            }
        ]

        response = self.app.get(API_ROOT_URL + '/feature-request')
        response_test = json.loads(response.data)
        self.assertEqual({'feature_requests': expected}, response_test)

    # Test for GET /feature-request, should get a single feature request
    def test_api_can_read_feature_request(self):
        FeatkeeperTestUtils.destroy_test_db()
        FeatkeeperTestUtils.populate_test_feature_requests()
        FeatkeeperTestUtils.populate_test_users()
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
        response = self.app.get(API_ROOT_URL + '/feature-request/56d3d524402e5f1cfc273340')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    # Test for PUT /feature-request, should create a new feature request and
    # return success message
    def test_api_can_create_feature_requests(self):
        FeatkeeperTestUtils.destroy_test_db()
        FeatkeeperTestUtils.populate_test_feature_requests()
        FeatkeeperTestUtils.populate_test_users()
        new_feature_request = {
            'title': 'Add end to end encripted chat',
            'description': 'Client wants to be able to send P2P encrypted messages to customers in realtime',
            'client_name': 'Akbar Erickssohn',
            'client_priority': 1,
            'target_date': '2016-10-29',
            'product_area': 'Policies',
            'agent_name': 'Eleuthere'
        }
        expected = {
            'status': 'success',
            'message': 'Feature request added'
        }
        response = self.app.post(
            API_ROOT_URL + '/feature-request',
            data=json.dumps(new_feature_request),
            content_type='application/json'
        )
        response_test = json.loads(response.data)
        del response_test['feature_request']
        self.assertEqual(expected, response_test)

    # Test for POST /feature-request, should edit an existing request and
    # return success message
    def test_api_can_update_feature_requests(self):
        FeatkeeperTestUtils.destroy_test_db()
        FeatkeeperTestUtils.populate_test_feature_requests()
        FeatkeeperTestUtils.populate_test_users()
        edit_feature_request = {
            '_id': '56d3d524402e5f1cfc273340',
            'client_priority': 3,
            'product_area': 'Billing',
        }
        expected = {
            'status': 'success',
            'message': 'Feature request updated'
        }
        response = self.app.put(
            API_ROOT_URL + '/feature-request/56d3d524402e5f1cfc273340',
            data=json.dumps(edit_feature_request),
            content_type='application/json'
        )
        response_test = json.loads(response.data)
        self.assertIsNot(None, response_test['feature_request']['modified_at'])
        self.assertEqual(3, response_test['feature_request']['client_priority'])
        self.assertEqual('Policies', response_test['feature_request']['product_area'])
        del response_test['feature_request']
        self.assertEqual(expected, response_test)

    # Test can authenticate user using token generation
    def test_api_can_authenticate_user(self):
        self.fail('test_api_deny_restricted_endpoints not finished!')

    # Test can deny API requests without valid authentication as admin
    def test_api_can_deny_requests_for_restricted_admin_endpoints(self):
        self.fail('test_api_can_deny_requests_for_restricted_admin_endpoints not finished!')

    # Test can deny API requests without valid authentication as agent
    def test_api_can_deny_requests_for_restricted_agent_endpoints(self):
        self.fail('test_api_can_deny_requests_for_restricted_agent_endpoints not finished!')

    # Test for non-existent API endpoint request should return error
    def test_api_non_existent_endpoint(self):
        expected = {
            'status': 'error',
            'message': 'Endpoint does not exist'
        }
        response = self.app.post(API_ROOT_URL + '/je-nexiste-pas')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

if __name__ == '__main__':
    unittest.main()
