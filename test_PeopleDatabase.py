from PeopleDatabase import PeopleDatabase
import unittest

class TestPeopleDatabase(unittest.TestCase):

    def setUp(self):
        self.db = PeopleDatabase()

if __name__ == '__main__':
    unittest.main()