import unittest
from number_guessing import guessing_game

class NumberGuessingTestClass(unittest.TestCase):
    """
    This class will be used to test the number guessing game method
    """

    def test_expect_result_to_be_in_valid_range(self):
        """
        Here lets test the number_guessing and ensure values are
        in the range of 0 to 100
        """
        result_1 = guessing_game()
        self.assertTrue(
            0 < result_1 <= 100, 
            msg="""Number guessing game should 
            predict values in range of 0 to 100""")

if __name__ == '__main__':
    unittest.main(verbosity=2)
