import unittest
import json
import copy
from app import app
from routes import *

class TestRoutesPUT(unittest.TestCase):
    """
    A test class for the PUT routes of the API.
    """

    def setUp(self):
        """
        Sets up the test client.  
        """
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
        """
        This test checks whether a person can be successfully updated by
        sending a PUT request to the '/people/{id}' endpoint with valid data.   
        """
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

    def test_update_person_not_found_for_unknown_id(self):
        """
        This test checks if 404 is returned when sending a PUT request to 
        the '/people/{id}' endpoint with unknown id.   
        """
        response = self.client.put(
            '/people/unknown_id',
            data = json.dumps(self.person_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_update_person_with_another_id(self):
        """
        This test checks if 400 is returned when sending a PUT request to 
        the '/people/{id}' endpoint when a 'id' field is included inside the
        data, and that id is already taken by someone else in the database..   
        """
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(self.person_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_update_person_with_an_email_already_taken(self):
        """
        This test checks if 400 is returned when sending a PUT request to 
        the '/people/{id}' endpoint when a 'email' field is included inside 
        the data, and that email is already taken by someone else in the database. 
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['email'] = 'janedoe@example.com'
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_update_person_with_firstName_set_to_empty_str(self):
        """
        This test checks if 400 is returned when sending a PUT request to
        the '/people/{id}' endpoint when a 'firstName' field is included, 
        but its value is empty.  
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['firstName'] = ''
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_update_person_with_firstName_set_to_invalid_format(self):
        """
        This test checks if 400 is returned when sending a PUT request to
        the '/people/{id}' endpoint when a 'firstName' field is included, 
        but its value is invalid format.  
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['firstName'] = '!nv@lid'
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        
    def test_update_person_with_lastName_set_to_empty_str(self):
        """
        This test checks if 400 is returned when sending a PUT request to
        the '/people/{id}' endpoint when a 'lastName' field is included, 
        but its value is empty.  
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['lastName'] = ''
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_update_person_with_lastName_set_to_invalid_format(self):
        """
        This test checks if 400 is returned when sending a PUT request to
        the '/people/{id}' endpoint when a 'lastName' field is included, but 
        its value is invalid format.  
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['lastName'] = '!nv@lid'
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)


    def test_update_person_with_email_set_to_empty_str(self):
        """
        This test checks if 400 is returned when sending a PUT request to
        the '/people/{id}' endpoint when a 'email' field is included, but 
        its value is empty.  
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['email'] = ''
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)

    
    def test_update_person_with_email_set_to_invalid_format(self):
        """
        This test checks if 400 is returned when sending a PUT request to
        the '/people/{id}' endpoint when a 'email' field is included, but
        its value is invalid format.  
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['email'] = 'wrong,,format@gmail!com'
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        
    def test_update_person_with_birthday_set_to_empty_str(self):
        """
        This test checks if 400 is returned when sending a PUT request to
        the '/people/{id}' endpoint when a 'birthday' field is included, 
        but its value is empty.  
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['birthday'] = ''
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_update_person_with_birthday_set_to_future_date(self):
        """
        This test checks if 400 is returned when sending a PUT request to
        the '/people/{id}' endpoint when a 'birthday' field is included, but 
        its value is a future date.  
        """
        invalid_person = copy.deepcopy(self.person_data)
        invalid_person.pop('id')
        invalid_person['birthday'] = '3500-01-01'
        response = self.client.put(
            '/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de',
            data=json.dumps(invalid_person),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        
if __name__ == "__main__":
    unittest.main()