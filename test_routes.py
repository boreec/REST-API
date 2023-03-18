import unittest
import json
from app import app
from routes import *

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
        result = self.client.get('/people/unknown-id')
        self.assertEqual(result.status_code, 404)

    
    def test_get_person_age_200(self):
        result = self.client.get('/people/bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de')
        self.assertEqual(result.status_code, 200)
        self.assertEqual('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de', json.loads(result.data)['id'])

if __name__ == '__main__':
    unittest.main()