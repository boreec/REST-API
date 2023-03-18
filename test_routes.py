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
        
if __name__ == '__main__':
    unittest.main()