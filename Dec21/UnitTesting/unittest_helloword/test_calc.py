import unittest

class TestClass01(unittest.TestCase):

    def test_understand_unittesting_pass(self):
        """
        Intentionally passing the test
        """
        result = 10>5
        self.assertTrue( result, "resut should be True")
    
    def test_understand_unittesting_fail(self):
        """
        Fail the test intenionally
        """
        result = 10 > 100
        self.assertTrue( result, "resut should be True")



if __name__ == '__main__':
    unittest.main()
