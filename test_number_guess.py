import unittest
from unittest.mock import patch
import numberGame
from tud_test_base import set_keyboard_input,get_display_output


class gameTest(unittest.TestCase):
    #test for valid user input
    def test_type_int(self):
        set_keyboard_input([34])
        numberGame.user_guess()
        output=get_display_output()
        self.assertEqual(numberGame.user_guess_validation(),'valid')

    #test for wrong data type of user input
    def test_ivalid_guess(self):
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
        
    #test for correct phone number input
    def test_phone_number_right(self):
        set_keyboard_input(['+254797661925'])
        numberGame.enter_phone()
        output=get_display_output()
        self.assertIs(numberGame.phone_validation(),True)


if __name__=="__main__":
    unittest.main()
