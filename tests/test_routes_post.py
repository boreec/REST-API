import unittest
import json
import copy
from app import app
from routes import *

class TestRoutesPOST(unittest.TestCase):
    """
    A test class for the POST routes of the API.
    """
    
    def setUp(self):
        """
        Sets up the test environment by creating a Flask test 
        client and enabling testing mode.  
        """
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
        """
        This test checks whether a person can be successfully created by
        sending a POST request to the '/people' endpoint with valid data.   
        """
        result = self.client.post('/people', 
            data=json.dumps(self.person_data), 
            content_type='application/json')
        
        self.assertEqual(result.status_code, 200)
        created_person = json.loads(result.data)
        self.assertEqual(self.person_data, created_person)

    def test_create_person_fails_for_id_set_to_None(self):
        """
        This test checks whether a person creation fails if the 'id' field
        in the person data is set to None.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['id'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_id_set_to_empty_str(self):
        """
        This test checks whether a person creation fails if the 'id' field 
        in the person data is set to an empty string.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['id'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_id_set_to_invalid_uuid_format(self):
        """
        This test checks whether a person creation fails if the 'id' field
        in the person data is set to an invalid UUID format.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['id'] = "02830-238028-308838-dsndsds"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_id_already_taken(self):
        """
        This test checks whether a person creation fails if the 'id' field 
        in the person data is already taken by someone else.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['id'] = "bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_firstName_set_to_None(self):
        """
        This test checks whether a person creation fails if the 'firstName' field
        in the person data is set to None.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['firstName'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_firstName_set_to_empty_str(self):
        """
        This test checks whether a person creation fails if the 'firstName' field
        in the person data is set to an empty string.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['firstName'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_firstName_set_to_invalid_name_format(self):
        """
        This test checks whether a person creation fails if the 'firstName' field 
        in the person data is set to an invalid name format.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['firstName'] = "W@lt3rZ"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_lastName_set_to_None(self):
        """
        This test checks whether a person creation fails if the 'lastName' field 
        in the person data is set to None.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['lastName'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_lastName_set_to_empty_str(self):
        """
        This test checks whether a person creation fails if the 'lastName' field 
        in the person data is set to an empty string.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['lastName'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_lastName_set_to_invalid_name_format(self):
        """
        This test checks whether a person creation fails if the 'lastName' field 
        in the person data is set to an invalid name format.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['lastName'] = "Sm!sth"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_email_set_to_None(self):
        """
        This test checks whether a person creation fails if the 'email' field in 
        the person data is set to None
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['email'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_email_set_to_empty_str(self):
        """
        This test checks whether a person creation fails if the 'email' field 
        in the person data is set to empty string.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['email'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_email_set_to_invalid_email_format(self):
        """
        This test checks whether a person creation fails if the 'email' field in
        the person data is set to invalid email format.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['email'] = "inval...id@em;ail@format.com"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_email_already_taken(self):
        """
        This test checks whether a person creation fails if the 'email' field 
        in the person data is set to an email that is already taken by someone else.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['email'] = "johndoe@example.com"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_birthday_set_to_None(self):
        """
        This test checks whether a person creation fails if the 'birthday' field
        in the person data is set to None
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = None
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_create_person_fails_for_birthday_set_to_empty_str(self):
        """
        This test checks whether a person creation fails if the 'birthday' field
        in the person data is set to an empty string.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = ""
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_birthday_set_to_future_date(self):
        """
        This test checks whether a person creation fails if the 'birthday' field
        in the person data is set to a future date.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = "3230-01-01"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)

        
    def test_create_person_fails_for_birthday_set_to_too_old_date(self):
        """
        This test checks whether a person creation fails if the 'birthday' field
        in the person data is set to a date too old for a living human.
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = "1800-01-01"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
    def test_create_person_fails_for_birthday_set_to_impossible_date(self):
        """
        This test checks whether a person creation fails if the 'birthday' field
        in the person data is set to a date with a good format but that can not
        be happen in real life (like a 29 february on a wrong year).
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person['birthday'] = "1998-02-29"
        result = self.client.post('/people', 
            data=json.dumps(invalid_person), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)
        
if __name__ == "__main__":
    unittest.main()