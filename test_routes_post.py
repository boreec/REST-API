import unittest
import json
from app import app
from routes import *

class TestRoutesPOST(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        
    def test_create_person_success(self):
        person_data = dict(
            id = "9d0e6be3-18e1-4e77-96ac-2e9260babe74",
            firstName = "Jack",
            lastName="Sparrow",
            email="jacksparrow@pirates.com",
            birthday="2000-10-23"
        )
               
        result = client_rw.post('/people', 
            data=json.dumps(person_data), 
            content_type='application/json')
        
        self.assertEqual(result.status_code, 200)
        created_person = json.loads(result.data)
        self.assertEqual(person_data, created_person)

    
