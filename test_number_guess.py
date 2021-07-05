from io import StringIO
import unittest
import numberGame
from unittest.mock import patch


class gameTest(unittest.TestCase):

    #test for wrong data type of user input
    def test_type_str(self):
        #mock user input
        with patch('numberGame.user_guess') as user_guess :
            user_guess.return_value='fff'
            self.assertEqual(numberGame.user_guess_validation(),'invalid')
            

    #test for the range of input
    def test_range_within(self):
        #mock user input
        with patch('numberGame.user_guess') as user_guess:
            user_guess.return_value=34
            #test if range is between 1-100
            self.assertTrue(0 <= numberGame.user_guess() <=100)
    
    #test for range over 100
    def test_range_above_100(self):
        #mock user input
        with patch('numberGame.user_guess') as user_guess:
            user_guess.return_value=101
            #test if range is between 1-100
            self.assertFalse(0 <= numberGame.user_guess() <=100)
    


if __name__=="__main__":
    unittest.main()