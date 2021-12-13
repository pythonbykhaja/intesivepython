import unittest
from puzzle import guessing_game, pig_latin

class PuzzleTestClass(unittest.TestCase):
    """
    This class will be used to test the puzzles
    
    """

    def test_guessing_game(self):
        """
        Here lets test the number_guessing and ensure values are
        in the range of 0 to 100
        """
        result_1 = guessing_game()
        self.assertTrue(
            0 < result_1 <= 100, 
            msg="""Number guessing game should 
            predict values in range of 0 to 100""")


    def test_pig_latin(self):
        """
        This method will test the pig_latin sequencs
        """
        words = ['python', 'air', 'eat', 'computer', '', 'a', 'b']
        expected_results = ['ythonpay', 'airway', 'eatway', 'omputercay', '', 'away', 'bay']
        self.assertEqual(len(words), len(expected_results), msg="Input is wrong")
        for index in range(len(words)):
            actual_result = pig_latin(words[index])
            self.assertEqual(
                actual_result, 
                expected_results[index], 
                msg=f"Pig Latin sequence is not working for {words[index]}"
            )


        


if __name__ == '__main__':
    unittest.main(verbosity=2)
