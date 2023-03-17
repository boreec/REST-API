from PeopleDatabase import PeopleDatabase
from Person import Person
import unittest

class TestPeopleDatabase(unittest.TestCase):

    def setUp(self):
        self.db = PeopleDatabase()

    def test_select_all_persons(self):
        rows = self.db.select_all_persons()
        self.assertEqual(4, len(rows))
        for person in rows :
            self.assertTrue(isinstance(person, Person))
            try:
                person.verify_id()
                person.verify_firstName()
                person.verify_lastName()
                person.verify_email()
                person.verify_birthday()
            except Exception:
                self.fail("Data retrieved from database is wrong format!")
        
if __name__ == '__main__':
    unittest.main()