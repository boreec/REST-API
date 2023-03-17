from Person import Person
import unittest

class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(self):        
        self.p1 = Person('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de','John','Doe','johndoe@example.com','1997-01-01')
        self.p2 = Person('d5356358-b39f-4c6e-9690-2c965a607702','Jane','Doe','janedoe@example.com','1991-07-28')

    def test_to_tuple(self):
        t = self.p1.to_tuple()
        self.assertTrue(isinstance(t, tuple))
        self.assertEqual(t[0], self.p1['id'])
        self.assertEqual(t[1], self.p1['firstName'])
        self.assertEqual(t[2], self.p1['lastName'])
        self.assertEqual(t[3], self.p1['email'])
        self.assertEqual(t[4], self.p1['birthday'])
                    
if __name__ == '__main__':
    unittest.main()