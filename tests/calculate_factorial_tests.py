import unittest
from exercises.calculate_factorial import *


class MyTestCase(unittest.TestCase):
    def test_zero_input_factorial_recursive(self):
        result = factorial_recursive(0)
        self.assertEqual(result, 1)

    def test_one_input_factorial_recursive(self):
        result = factorial_recursive(1)
        self.assertEqual(result, 1)

    def test_negative_process_input(self):
        value, error_message = process_input("-7")
        self.assertIsNone(value)
        self.assertEqual(error_message, "Number cannot be negative.")

    def test_fraction_process_input(self):
        value, error_message = process_input("3.3")
        self.assertIsNone(value)
        self.assertEqual(error_message, "Number must be an integer.")

    def test_positive_number_process_input(self):
        value, error_message = process_input("5")
        self.assertEqual(value, 5)
        self.assertEqual(error_message, '')

    def test_large_number_process_input(self):
        value, error_message = process_input("20")
        self.assertEqual(value, 20)
        self.assertEqual(error_message, '')

    def test_number_right_above_recursion_limit_process_input(self):
        value, error_message = process_input("999")
        recur_limit = sys.getrecursionlimit()-1
        self.assertEqual(value, None)
        self.assertEqual(error_message, "Number must be lower than" + str(recur_limit) + " for our calculation.")

    def test_number_right_below_recursion_limit_process_input(self):
        number=sys.getrecursionlimit()-2
        value, error_message = process_input(str(number))
        self.assertEqual(value, number)
        self.assertEqual(error_message, '')


if __name__ == '__main__':
    unittest.main()
