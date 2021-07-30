import unittest
from unittest import result
from fibo import fibonacci

class TestFibonacci(unittest.TestCase):
    """This TestCase will test the fibonacci functionality

    """

    def test_fibo_zero_index(self):
        """
        This test step will test the zero index of fibonacci
        """
        result = fibonacci(0)
        self.assertEqual(result , 0, "Result should be zero")
        
    def test_fibo_first_index(self):
        """
        This test step will test the first index of fibonacci
        """
        result = fibonacci(1)
        self.assertEqual(result, 1, "Result should be one")

    def test_fibo_other_indexes(self):
        """
        This test step will test the fibonnaci with other indexes
        """
        result = fibonacci(2)
        self.assertEqual(result, 1, "Result should be one")
        result = fibonacci(3)
        self.assertEqual(result, 2)
        result = fibonacci(4)
        self.assertEqual(result, 3)



if __name__ == '__main__':
    unittest.main()