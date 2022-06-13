import unittest
import add_function

class TestAddFunction(unittest.TestCase):

    def test_add_two_positive_numbers(self):
        result = add_function.add(7, 17)

        self.assertEqual(result, 24)
    

    def test_add_two_negative_numbers(self):
        result = add_function.add(-8, -22)

        self.assertEqual(result, -30)


    def test_add_zero_to_negative_number(self):
        result = add_function.add(-8, 0)

        self.assertEqual(result, -8)


    def test_add_positive_to_negative_number(self):
        result = add_function.add(-8, 12)

        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()