import unittest


class TestString(unittest.TestCase):
    def setUp(self):
        pass

    # returns True if the string contains 4  a.
    def test_strings(self):
        self.assertEquals('a' * 4, 'aaaa')

    # returns TRUE if the string is in uppercase
    def test_upper(self):
        self.assertEquals('foo'.upper(), 'FOO')

    # return TRUE if the string is un uppercase, else returns FALSE
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
