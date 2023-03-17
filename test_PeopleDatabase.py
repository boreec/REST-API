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

    def test_select_person_by_id(self):
        # test None is returned for unknown id.
        self.assertEqual(None, self.db.select_person_by_id("41f7ad9c-0e21-43c9-bd8e-2678fe421232"))

        person = self.db.select_person_by_id("bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de")

        self.assertTrue(isinstance(person, Person))
        self.assertEqual("bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", person['id'])

    def test_select_person_by_email(self):
        # test None is returned for unknown email.
        self.assertEqual(None, self.db.select_person_by_email("unknown@email.com"))

        person = self.db.select_person_by_email("johndoe@example.com")

        self.assertTrue(isinstance(person, Person))
        self.assertEqual("johndoe@example.com", person['email'])
    
if __name__ == '__main__':
    unittest.main()