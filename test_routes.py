import unittest
from app import app
from routes import *

class RoutesTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

if __name__ == '__main__':
    unittest.main()