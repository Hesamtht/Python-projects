import unittest
import time

class Person:
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def email(self):
        return f"{self.fullname()}@gmail.com".replace(' ' , '')

person1 = Person('hesam' , 'mozafari')

#also you can test this class by creating new file and import Person (from unit-test import Person)

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('hesam' , 'mzf')
        self.p2 = Person('ali' , 'ahmadi')

    def test_fullname(self):
        self.assertEqual(self.p1.fullname() , 'hesam mzf')
        self.assertEqual(self.p2.fullname() , 'ali ahmadi')
        time.sleep(2)

    def test_email(self):
        self.assertEqual(self.p1.email() , 'hesammzf@gmail.com')
        self.assertEqual(self.p2.email() , 'aliahmadi@gmail.com')

if __name__ == '__main__':
    unittest.main()