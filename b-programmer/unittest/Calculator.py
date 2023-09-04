import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator()

    def test_add(self):
        result = self.cal.add(1, 2)
        self.assertEquals(result, 3)

    def test_subtract(self):
        result = self.cal.subtract(3, 1)
        self.assertEquals(result, 2)

    def test_multiply(self):
        result = self.cal.multiply(3, 4)
        self.assertEquals(result, 12)

    def test_divide(self):
        result = self.cal.divide(3, 1)
        self.assertEquals(result, 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.cal.divide(3, 0)


if __name__ == '__main__':
    unittest.main()
