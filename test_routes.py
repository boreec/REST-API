import unittest
import json
from app import app
from routes import *
from datetime import date

class RoutesTest(unittest.TestCase):

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

    def test_get_people_with_name_starting_with_empty_prefix(self):
        result = self.client.get('/people?name=')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(4, len(json.loads(result.data)))
        self.assertTrue(json.loads(result.data)[0]['firstName'] == 'John')
        self.assertTrue(json.loads(result.data)[1]['firstName'] == 'Jane')
        self.assertTrue(json.loads(result.data)[2]['firstName'] == 'Brian')
        self.assertTrue(json.loads(result.data)[3]['firstName'] == 'Ashley')

    def test_get_people_with_name_starting_with_unknown_prefix(self):
        result = self.client.get("/people?name=\'unknown_prefix\'")
        self.assertEqual(result.status_code, 200)
        self.assertTrue(json.loads(result.data) == [])
        
if __name__ == '__main__':
    unittest.main()