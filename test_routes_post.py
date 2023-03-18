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

    def test_create_person_fails_for_id_set_to_None(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['id'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_id_set_to_empty_str(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['id'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_id_set_to_invalid_uuid_format(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['id'] = "02830-238028-308838-dsndsds"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_id_already_taken(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['id'] = "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_firstName_set_to_None(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['firstName'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_firstName_set_to_empty_str(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['firstName'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_firstName_set_to_invalid_name_format(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['firstName'] = "W@lt3rZ"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_lastName_set_to_None(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['lastName'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_lastName_set_to_empty_str(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['lastName'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_lastName_set_to_invalid_name_format(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['lastName'] = "Sm!sth"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_email_set_to_None(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['email'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_email_set_to_empty(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['email'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_email_set_to_invalid_email_format(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['email'] = "inval...id@em;ail@format.com"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_email_already_taken(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['email'] = "johndoe@example.com"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_birthday_set_to_None(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_birthday_set_to_empty_str(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_birthday_set_to_future_date(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = "3230-01-01"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

        
    def test_create_person_fails_for_birthday_set_to_too_old_date(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = "1800-01-01"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_birthday_set_to_impossible_date(self):
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = "1998-02-29"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
if __name__ == "__main__":
    unittest.main()