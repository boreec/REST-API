import unittest

class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):        
        self.p1 = Person('bf552a1c-fd73-4bd0-b64a-d3f69a9ff9de','John','Doe','johndoe@example.com','1997-01-01')
        self.p2 = Person('d5356358-b39f-4c6e-9690-2c965a607702','Jane','Doe','janedoe@example.com','1991-07-28')
    
if __name__ == '__main__':
    unittest.main()