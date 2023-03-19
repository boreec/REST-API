import unittest
import json
import copy
from app import app
from routes import *

class TestRoutesPUT(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        self.person_data = dict(
            id = "9d0e6be3-18e1-4e77-96ac-2e9260babe74",
            firstName = "Matthew",
            lastName="Grant",
            email="MatthewGrant@example.com",
            birthday="2000-10-23"
        )

    def test_update_person_success(self):
        valid_person = copy.deepcopy(self.person_data)
        valid_person.pop('id')
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(valid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.person_data['firstName'], json.loads(response.data)['firstName'])
        self.assertEqual(self.person_data['lastName'], json.loads(response.data)['lastName'])
        self.assertEqual(self.person_data['birthday'], json.loads(response.data)['birthday'])
        
if __name__ == "__main__":
    unittest.main()