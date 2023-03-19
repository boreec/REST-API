import unittest
import json
from app import app
from routes import *

class TestRoutesPUT(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        self.person_data = dict(
            id = "9d0e6be3-18e1-4e77-96ac-2e9260babe74",
            firstName = "Jack",
            lastName="Sparrow",
            email="jacksparrow@pirates.com",
            birthday="2000-10-23"
        )
        
        
if __name__ == "__main__":
    unittest.main()