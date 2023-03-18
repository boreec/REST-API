# -*- coding: utf-8 -*-

import unittest
import json
from app import app
from routes import *
from datetime import date

class TestRoutesGET(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        
    def test_get_people(self):
        result = self.client.get('/people')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(4, len(json.loads(result.data)))

    def test_get_person_by_id_404(self):
        result = self.client.get('/people/unknown-id')
        self.assertEqual(result.status_code, 404)

    def test_get_person_by_id_200(self):
        result = self.client.get('/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de')
        self.assertEqual(result.status_code, 200)
        self.assertEqual('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de', json.loads(result.data)['id'])

    def test_get_person_age_404(self):
        result = self.client.get('/people/unknown-id/age')
        self.assertEqual(result.status_code, 404)
  
    def test_get_person_age_200(self):
        result = self.client.get('/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de/age')
        self.assertEqual(result.status_code, 200)

    def test_get_person_age_200_correct_age(self):
        result = self.client.get('/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de/age')
        self.assertEqual(date.today().year - 1997, int(result.data))

    def test_get_people_with_name_starting_with_j(self):
        result = self.client.get("/people?name=j")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(2, len(json.loads(result.data)))
        self.assertTrue(json.loads(result.data)[0]['firstName'] == 'John')
        self.assertTrue(json.loads(result.data)[1]['firstName'] == 'Jane')

    def test_get_people_with_name_starting_with_ja(self):
        result = self.client.get("/people?name=ja")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(1, len(json.loads(result.data)))
        self.assertTrue(json.loads(result.data)[0]['firstName'] == 'Jane')
        
    def test_get_people_with_name_starting_with_empty_prefix(self):
        result = self.client.get('/people?name=')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(4, len(json.loads(result.data)))
        self.assertTrue(json.loads(result.data)[0]['firstName'] == 'John')
        self.assertTrue(json.loads(result.data)[1]['firstName'] == 'Jane')
        self.assertTrue(json.loads(result.data)[2]['firstName'] == 'Brian')
        self.assertTrue(json.loads(result.data)[3]['firstName'] == 'Ashley')

    def test_get_people_with_name_starting_with_unknown_prefix(self):
        result = self.client.get("/people?name=unknown_prefix")
        self.assertEqual(result.status_code, 200)
        self.assertTrue(json.loads(result.data) == [])

# class TestCreatePerson(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         self.client = app.test_client()
        
#     def test_create_person_success(self):
#         person_data = dict(
#             id = "9d0e6be3-18e1-4e77-96ac-2e9260babe74",
#             firstName = "Jack",
#             lastName="Sparrow",
#             email="jacksparrow@pirates.com",
#             birthday="2000-10-23"
#         )
        
#         client_rw = app.test_client()
        
#         result = client_rw.post('/people', 
#             data=json.dumps(person_data), 
#             content_type='application/json')
        
#         print(result.data)
#         self.assertEqual(result.status_code, 200)
#         created_person = json.loads(result.data)
#         self.assertEqual(person_data, created_person)

if __name__ == '__main__':
    unittest.main()