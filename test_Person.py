from Person import Person
import unittest

class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(self):        
        self.p1 = Person('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de','John','Doe','johndoe@example.com','1997-01-01')

    def test_to_tuple(self):
        t = self.p1.to_tuple()
        self.assertTrue(isinstance(t, tuple))
        self.assertEqual(t[0], self.p1['id'])
        self.assertEqual(t[1], self.p1['firstName'])
        self.assertEqual(t[2], self.p1['lastName'])
        self.assertEqual(t[3], self.p1['email'])
        self.assertEqual(t[4], self.p1['birthday'])

    def test_verify_id_raises_exception(self):
        self.assertRaises(Exception, Person(None, "","", "","").verify_id)
        self.assertRaises(Exception, Person("", "","", "","").verify_id)
        self.assertRaises(Exception, Person("invalid-format", "","", "","").verify_id)

    def test_verify_id_good_format(self):
        try:
            Person('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de','','','','').verify_id()
        except Exception:
            self.fail("Person.verify_id() raised Exception for good uuid format.")

    def test_verify_firstName_raises_exception(self):
        self.assertRaises(Exception, Person("", None, "", "", "").verify_firstName)
        self.assertRaises(Exception, Person("", "", "", "", "").verify_firstName)
        self.assertRaises(Exception, Person("", "!nv@lidN@m3", "", "", "").verify_firstName)

    def test_verify_firstName_good_format(self):
        try:
            Person('','John','','','').verify_firstName()
        except Exception:
            self.fail("Person.verify_firstName() raised Exception for good name format.")

    def test_verify_lastName_raises_exception(self):
        self.assertRaises(Exception, Person("", "", None, "", "").verify_lastName)
        self.assertRaises(Exception, Person("", "", "", "", "").verify_lastName)
        self.assertRaises(Exception, Person("", "" ,"!nv@lidN@m3", "", "").verify_lastName)

    def test_verify_lastName_good_format(self):
        try:
            Person('','','Smith','','').verify_lastName()
        except Exception:
            self.fail("Person.verify_lastName() raised Exception for good name format.")

    def test_verify_email_raises_exception(self):
        self.assertRaises(Exception, Person("","","",None,"").verify_email)
        self.assertRaises(Exception, Person("","","","","").verify_email)
        self.assertRaises(Exception, Person("","","","test@test@.com","").verify_email)
        self.assertRaises(Exception, Person("","","","@:@:gmail.com","").verify_email)

    def test_verify_email_good_format(self):
        try:
            Person('','','', 'johndoe@example.com','').verify_email()
            Person('','','', 'a@b.cd','').verify_email()
        except Exception as e:
            self.fail("Person.verify_email() raised exception for good name format")
            
if __name__ == '__main__':
    unittest.main()