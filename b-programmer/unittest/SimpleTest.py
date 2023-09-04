import unittest


class SimpleTest(unittest.TestCase):
    # returns True or False
    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
