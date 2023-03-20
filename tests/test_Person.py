# Author: Cyprien Borée boreec@tuta.io

from core.Person import Person
import unittest

class TestPerson(unittest.TestCase):
    """
    A class that ensure good behaviour for class People
    by testing its functions.
    """
    def test_to_tuple(self):
        """
        Test case for to_tuple function returning the good data.  
        """
        p1 = Person('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de','John','Doe','johndoe@example.com','1997-01-01')
        t = p1.to_tuple()
        self.assertTrue(isinstance(t, tuple))
        self.assertEqual(t[0], p1['id'])
        self.assertEqual(t[1], p1['firstName'])
        self.assertEqual(t[2], p1['lastName'])
        self.assertEqual(t[3], p1['email'])
        self.assertEqual(t[4], p1['birthday'])

    def test_verify_id_raises_exception(self):
        """
        Test case for verify_id function raising an Exception if the 
        id does not have a good value or format.  
        """
        self.assertRaises(Exception, Person(None, "","", "","").verify_id)
        self.assertRaises(Exception, Person("", "","", "","").verify_id)
        self.assertRaises(Exception, Person("invalid-format", "","", "","").verify_id)

    def test_verify_id_good_format(self):
        """
        Test case for verify_id function to verify an id has a good format. 
        """
        try:
            Person('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de','','','','').verify_id()
        except Exception:
            self.fail("Person.verify_id() raised Exception for good uuid format.")

    def test_verify_firstName_raises_exception(self):
        """
        Test case for verify_firstName function raising an Exception if the
        firstName does not have a good value or format. 
        """
        self.assertRaises(Exception, Person("", None, "", "", "").verify_firstName)
        self.assertRaises(Exception, Person("", "", "", "", "").verify_firstName)
        self.assertRaises(Exception, Person("", "!nv@lidN@m3", "", "", "").verify_firstName)

    def test_verify_firstName_good_format(self):
        """
        Test case for verify_firstName function to verify a firstName with a good format.  
        """
        try:
            Person('','John','','','').verify_firstName()
        except Exception:
            self.fail("Person.verify_firstName() raised Exception for good name format.")

    def test_verify_lastName_raises_exception(self):
        """
        Test case for verify_lastName function raising an Exception if the
        lastName does not have a good value or format. 
        """
        self.assertRaises(Exception, Person("", "", None, "", "").verify_lastName)
        self.assertRaises(Exception, Person("", "", "", "", "").verify_lastName)
        self.assertRaises(Exception, Person("", "" ,"!nv@lidN@m3", "", "").verify_lastName)

    def test_verify_lastName_good_format(self):
        """
        Test case for verify_lastName function to verify a lastName with a good format.  
        """
        try:
            Person('','','Smith','','').verify_lastName()
        except Exception:
            self.fail("Person.verify_lastName() raised Exception for good name format.")

    def test_verify_email_raises_exception(self):
        """
        Test case for verify_email function raising an Exception if the
        email does not have a good value or format. 
        """
        self.assertRaises(Exception, Person("","","",None,"").verify_email)
        self.assertRaises(Exception, Person("","","","","").verify_email)
        self.assertRaises(Exception, Person("","","","test@test@.com","").verify_email)
        self.assertRaises(Exception, Person("","","","@:@:gmail.com","").verify_email)

    def test_verify_email_good_format(self):
        """
        Test case for verify_email function to verify a email with a good format.  
        """
        try:
            Person('','','', 'johndoe@example.com','').verify_email()
            Person('','','', 'a@b.cd','').verify_email()
        except Exception as e:
            self.fail("Person.verify_email() raised exception for good name format.")

    def test_verify_birthday_raises_exception(self):
        """
        Test case for verify_birthday function raising an Exception if the
        birthday does not have a good value or format. 
        """
        self.assertRaises(Exception, Person("","","","",None).verify_birthday)
        self.assertRaises(Exception, Person("","","","","").verify_birthday)
        self.assertRaises(Exception, Person("","","","","March 21st 1998").verify_birthday)
        self.assertRaises(Exception, Person("","","","","3000-01-01").verify_birthday)
        self.assertRaises(Exception, Person("","","","","1800-01-01").verify_birthday)
        self.assertRaises(Exception, Person("","","","","1998-13-01").verify_birthday)
        self.assertRaises(Exception, Person("","","","","1998-02-29").verify_birthday)

    def test_verify_birthday_good_format(self):
        """
        Test case for verify_birthday function to verify a email with a good format.  
        """
        try:
            Person('','','','','1998-12-01').verify_birthday()
            Person('','','','','1998-02-28').verify_birthday()
        except Exception:
            self.fail("Person.verify_birthday() raised exception for good birthday format.")

if __name__ == '__main__':
    unittest.main()