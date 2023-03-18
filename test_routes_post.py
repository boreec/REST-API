import unittest
import json
import copy
from app import app
from routes import *

class TestRoutesPOST(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.person_data = dict(
            id = "9d0e6be3-18e1-4e77-96ac-2e9260babe74",
            firstName = "Jack",
            lastName="Sparrow",
            email="jacksparrow@pirates.com",
            birthday="2000-10-23"
        )
        
    def test_create_person_success(self):
        result = self.client.post('/people', 
            data=json.dumps(self.person_data), 
            content_type='application/json')
        
        self.assertEqual(result.status_code, 200)
        created_person = json.loads(result.data)
        self.assertEqual(self.person_data, created_person)

    def test_create_person_fails_for_id(self):
        invalid_person = copy.deepcopy(self.person_data)
        # 1. Test for id set to None.
        invalid_person['id'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 2. Test for id set to empty string.
        invalid_person['id'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 3. Test for id not compliant to UUID v4 format.
        invalid_person['id'] = "02830-238028-308838-dsndsds"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_firstName(self):
        invalid_person = copy.deepcopy(self.person_data)
        # 1. Test for firstName set to None.
        invalid_person['firstName'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 2. Test for firstName set to empty string.
        invalid_person['firstName'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 3. Test for firstName set to invalid name format.
        invalid_person['firstName'] = "W@lt3rZ"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_lastName(self):
        invalid_person = copy.deepcopy(self.person_data)
        # 1. Test for lastName set to None.
        invalid_person['lastName'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 2. Test for lastName set to empty string.
        invalid_person['lastName'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 3. Test for lastName set to invalid name format.
        invalid_person['lastName'] = "Sm!sth"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_email(self):
        invalid_person = copy.deepcopy(self.person_data)
        # 1. Test for email set to None
        invalid_person['email'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 2. Test for email set to empty string.
        invalid_person['email'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 3. Test for email set to invalid email format.
        invalid_person['email'] = "inval...id@em;ail@format.com"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        # 4. Test for email set to already used email.
        invalid_person['email'] = "johndoe@example.com"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
if __name__ == "__main__":
    unittest.main()