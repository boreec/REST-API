import unittest
import json
import copy
from app import app
from routes import *

class TestRoutesDELETE(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_delete_person_success(self):
        temporary_person = dict(
            id="6e0f74c1-fbcd-4ea9-8faf-6b9d9fc14015",
            firstName="Jason",
            lastName="Statham",
            email="jasonstatham@yahoo.com",
            birthday="1967-07-26"
        )

        # Put a temporary person inside the database.  
        response = self.client.post(
            '/people', 
            data=json.dumps(temporary_person),
            mimetype='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), temporary_person)

        # Check that the person is inserted.
        response = self.client.get('/people/' + temporary_person['id'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), temporary_person)

        # Delete the person.
        response = self.client.delete('/people/' + temporary_person['id'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), temporary_person)

        # Check the person does not exist anymore
        response = self.client.get('/people/' + temporary_person['id'])
        self.assertEqual(response.status_code, 404)

        
if __name__ == "__main__":
    unittest.main()