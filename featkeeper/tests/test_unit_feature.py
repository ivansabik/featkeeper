# test_unit_feature.py

import sys
sys.path.append('/home/ivansabik/Desktop/featkeeper')
from featkeeper import schemas
import unittest

class FeatureRequestUnitTest(unittest.TestCase):
    def test_create_feature_request(self):
        pass

    def find_feature_request(self):
        pass

    def update_feature_request(self):
        pass

    def set_ticket_url(self):
        pass

    '''
    A numbered priority according to the client (1...n).
    Client Priority numbers should not repeat for the given client,
    so if a priority is set on a new feature as "1",
    then all other feature requests for that client should be reordered.
    '''
    def reassign_new_feature_request_client_priority(self):
        pass

if __name__ == '__main__':
    unittest.main()
