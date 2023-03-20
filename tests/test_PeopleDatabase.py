# Author: Cyprien Borée boreec@tuta.io

from core.PeopleDatabase import PeopleDatabase
from core.Person import Person
import unittest

class TestPeopleDatabase(unittest.TestCase):
    """
    A class to ensure good behaviour of the class PeopleDatabase,
    by testing its functions.
    """
    
    def setUp(self):
        """
        Create a new database attribute before running each unit test.
        """
        self.db = PeopleDatabase()

    def test_select_all_persons(self):
        """
        Test the select_all_persons() function of PeopleDatabase.
        """
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

    def test_select_person_by_id_for_unknown_id(self):
        """
        Test select_person_by_id() returns None when an unknown id is provided.  
        """
        self.assertEqual(None, self.db.select_person_by_id("41f7ad9c-0e21-43c9-bd8e-2678fe421232"))

    def test_select_person_by_id_for_known_id(self):
        """
        Test select_person_by_id() return a Person object corresponding to an existing id. 
        """
        person = self.db.select_person_by_id("bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de")
        self.assertTrue(isinstance(person, Person))
        self.assertEqual("bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de", person['id'])

    def test_select_person_by_email_for_unknown_email(self):
        """
        Test select_person_by_email returns None when an unknown email is provided.  
        """
        self.assertEqual(None, self.db.select_person_by_email("unknown@email.com"))

    def test_select_person_by_email_for_known_email(self):
        """
        Test select_person_by_email returns a Person object corresponding to an existing email.
        """
        person = self.db.select_person_by_email("johndoe@example.com")
        self.assertTrue(isinstance(person, Person))
        self.assertEqual("johndoe@example.com", person['email'])

    def test_select_persons_by_name_starting_with_unknown_prefix(self):
        """
        Test select_persons_by_name starting_with returns an empty list of Persons
        when the provided prefix does not correspond to anything in the table.  
        """
        self.assertEqual([], self.db.select_persons_by_name_starting_with("eazoieoaz"))

    def test_select_persons_by_name_sarting_with_empty_prefix(self):
        """
        Test select_persons_by_name_starting_with_empty_prefix returns a list of
        all the Persons when the provided prefix is empty.  
        """
        self.assertEqual(4, len(self.db.select_persons_by_name_starting_with("")))
    
    def test_select_persons_by_name_starting_with_j(self):
        """
        Test select_persons_by_name_starting_with() returns a list of all the
        Persons with their name starting with 'j'.
        """
        persons = self.db.select_persons_by_name_starting_with("j")
        self.assertEqual(2, len(persons))
        self.assertTrue(persons[0]['firstName'] == 'John' or persons[0]['firstName'] == 'Jane')
        self.assertTrue(persons[1]['firstName'] == 'John' or persons[1]['firstName'] == 'Jane')

    def test_update_person_with_unknown_person(self):
        """
        Test update_person returns None when the provided person is unknown. 
        """
        p = Person('???','???','???','???','???')
        self.assertEqual(None, self.db.update_person(p))

    def test_update_person_with_known_person(self):
        """
        Test update_person returns a Person object. 
        """
        person = self.db.select_person_by_id("bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de")
        # make sure of retrieved data
        self.assertEqual(person['firstName'], "John")

        # modify the person's name
        person['firstName'] = "Harry"
        self.db.update_person(person)

        person = self.db.select_person_by_id("bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de")
        # make sure retrieved data has been changed
        self.assertEqual(person['firstName'], "Harry")

    def test_delete_person_with_unknown_person(self):
        """
        Test delete_person returns None when the provided person is unknown.  
        """
        p = Person('???','???','???','???','???')

        persons_before_delete = self.db.select_all_persons()
        self.db.delete_person(p)
        persons_after_delete = self.db.select_all_persons()
        
        self.assertEqual(persons_before_delete, persons_after_delete)

    def test_delete_person_with_known_person(self):
        """
        Test delete_person returns the deleted person when a known person is provided.  
        """
        person = self.db.select_person_by_id("bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de")
        self.assertNotEqual(None, person)
        self.db.delete_person(person)
        person = self.db.select_person_by_id("bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de")
        self.assertEqual(None, person)
        
        
if __name__ == '__main__':
    unittest.main()