import unittest

class TestStringMethods(unittest.TestCase):

    #That test method .upper() is checking the string 'foo' correctly converts all characters to uppercase.
    # And it should be 'FOO'.
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper()) #Checking if 'FOO' is all uppercase. 
        self.assertFalse('Foo'.isupper()) #Checking if 'Foo' is all uppercase.

    #Checking the string 'hello world' is correctly split into a list of words using the default space separator.
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        #Checking by calling .split(2) raises a TypeError because the split() method expects a string as a separator, not an integer.
        with self.assertRaises(TypeError):
            s.split(2)

    #Checking the string '123' contains only digits, isdigit() should return True for this  test case.
    def test_isdigit(self):
        self.assertTrue('12i3'.isdigit())

if __name__ == '__main__':
    unittest.main()
