'''
test_unit_user.py
Tests User behaviour (find, save, validation methods, etc) for both agents and admins
'''

import os
import sys
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import unittest
from featkeeper.models import User
from utils import FeatkeeperTestUtils
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

class UserUnitTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        FeatkeeperTestUtils.populate_test_users()

    # Delete test db
    def tearDown(self):
        FeatkeeperTestUtils.destroy_test_db()

    # Test when instanced with default test parameter uses dev db
    def test_use_dev_db(self):
        user = User()
        self.assertEqual('featkeeper', user.db.name)

    # Test when instanced with test parameter actually uses test db
    def test_use_test_db(self):
        user = User(test=True)
        self.assertEqual('featkeeper_test', user.db.name)

    # Test when instanced with default params, user type is agent
    def test_default_is_agent(self):
        user = User(test=True)
        self.assertEqual(user.type, 'agent')

    # Test generate token with user type (agent or admin) and with expiration time
    def test_generate_token(self):
        user = User(test=True)
        user = user.find_by_username('dondiablo@gmx.de')
        token = user.get_token() # Detects test db mode from instance
        expected_decoded = {
            'username': 'dondiablo@gmx.de',
            'type': 'agent'
        }
        s = Serializer('NOT_SO_SECRET_KEY')
        decoded = s.loads(token)
        self.assertEqual(expected_decoded, decoded)

    # Test verify token is not valid
    def test_verify_token_invalid(self):
        invalid_fake_token = '1nv4lidT0k3n'
        token_is_valid = User.verify_token(invalid_fake_token)
        self.assertFalse(token_is_valid)

    # Test verify token is valid but expired
    def test_verify_token_valid_but_expired(self):
        s = Serializer('NOT_SO_SECRET_KEY', expires_in = 0)
        valid_expired_token = s.dumps(
            {
                'username': 'dondiablo@gmx.de',
                'type': 'agent'
            }
        )
        time.sleep(1)
        token_is_valid = User.verify_token(valid_expired_token)
        self.assertFalse(token_is_valid)

    # Test verify token is valid and not yet expired
    def test_verify_token_valid_and_not_expired(self):
        s = Serializer('NOT_SO_SECRET_KEY', expires_in = 30)
        valid_token = s.dumps(
            {
                'username': 'dondiablo@gmx.de',
                'type': 'agent'
            }
        )
        verify_result = User.verify_token(valid_token)
        expected = True
        self.assertEqual(expected, verify_result)

    def test_set_password(self):
        user = User(test=True)
        user.set_password('testSetPassword')
        self.assertRegexpMatches(user.hashim, 'pbkdf2:sha1:1000\$[a-zA-Z0-9_]{8}\$*[a-zA-Z0-9_]{40}')

    def test_verify_password(self):
        pass

    # Test user authentification for agents exiting username and pass
    def test_agent_auth_succesful(self):
        username = 'dondiablo@gmx.de'
        password = ''
        user_type = User.auth(username, password)
        self.assertEqual('agent', user_type)

    # Test user authentification for admins exiting username and pass
    def test_admin_auth_succesful(self):
        username = 'gary.host@ghost.com'
        password = ''
        user_type = User.auth(username, password)
        self.assertEqual('admin', user_type)

    # Test failed user authentification with wrong username and pass
    def test_auth_failed_wrong_credentials(self):
        username = 'dondiablo@gmx.de'
        password = 'NotMyActualPassword'
        user_type = User.auth(username, password)
        self.assertEqual('', user_type)

    # Test failed user authentification with valid creds but access disabled
    def test_auth_failed_user_disabled(self):
        username = 'mandel@muddypaws.org'
        password = ''
        user_type = User.auth(username, password)
        self.assertEqual('', user_type)

    @unittest.skip('')
    # Test find all agents
    def test_find_all_agents(self):
        self.fail('test_find_all_agents not finished!')

    @unittest.skip('')
    # Test find user by username
    def test_find_user_by_username(self):
        self.fail('test_find_user_by_username not finished!')

    @unittest.skip('')
    # Test create agent
    def test_create_user_agent_type(self):
        self.fail('test_create_user_agent_type not finished!')

    @unittest.skip('')
    # Test update existing agent
    def test_update_user_agent_type(self):
        self.fail('test_update_user_agent_type not finished!')

if __name__ == '__main__':
    unittest.main()
