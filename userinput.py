'''
@Author: Rashmi
@Date: 2021-09-28 23:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 1:30
@Title :Write a Python program test cases for user registration'''
from Regexvalid import Validation_User
import unittest
class TestMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_firstname_true(self):
        '''
        Description:
            The given valid first name returns true in this test case.
        '''
        self.assertTrue(Validation_User.validate_name("Ravali"))
        self.assertTrue(Validation_User.validate_name("Rashmi"))
        self.assertTrue(Validation_User.validate_name("Hruthik"))
        self.assertTrue(Validation_User.validate_name("Charishma"))

    def test_firstname_false(self):
        '''
        Description:
            The given invalid first name returns false in this test case.
        '''
        self.assertFalse(Validation_User.validate_name("he"))
        self.assertFalse(Validation_User.validate_name("rashmi@"))
        self.assertFalse(Validation_User.validate_name("X12#ews"))
        self.assertFalse(Validation_User.validate_name("S-hvani"))

    def test_Invalidfirstname_Raise_exception(self):   
        '''
        Desription:
            The given invalid first name should raise exception in this test case.
        '''
        self.assertRaises(Exception)

    def test_lastname_true(self):
        '''
        Description:
            The given valid last name returns true in this test case.
        '''
        self.assertTrue(Validation_User.validate_name("Pulmamidi"))
        self.assertTrue(Validation_User.validate_name("Cherry"))

    def test_lastname_false(self):
        '''
        Description:
            The given invalid last name returns false in this test case.
        '''
        self.assertFalse(Validation_User.validate_name("#pulmamidi"))
        self.assertFalse(Validation_User.validate_name("r@m"))

    def test_emailid_true(self):
        '''
        Description:
            The given valid email id returns true in this test case.
        '''
        self.assertTrue(Validation_User.validate_email("abc.xyz@bl.co.in"))
        self.assertTrue(Validation_User.validate_email("ras@gmail.com"))

    def test_emailid_false(self):
        '''
        Description:
            The given invalid email id returns false in this test case.
        '''
        self.assertFalse(Validation_User.validate_email("rashmi25@gmailcom"))
        self.assertFalse(Validation_User.validate_email("r@m"))

    def test_phonenumber_true(self):
        '''
        Description:
            The given valid phone number returns true in this test case.
        '''
        self.assertTrue(Validation_User.validate_phone_number("91 9812056239"))
        self.assertTrue(Validation_User.validate_phone_number("91 8954321208"))
        self.assertTrue(Validation_User.validate_phone_number("91 9892388991"))
        self.assertTrue(Validation_User.validate_phone_number("91 8923617777"))

    def test_phonenumber_false(self):
        '''
        Description:
            The given invalid phone number returns false in this test case.
        '''
        self.assertFalse(Validation_User.validate_phone_number("88 1235799021"))
        self.assertFalse(Validation_User.validate_phone_number("72125647389212"))
        self.assertFalse(Validation_User.validate_phone_number("12 9812780910"))
        self.assertFalse(Validation_User.validate_phone_number("72-2564738922"))
        self.assertFalse(Validation_User.validate_phone_number(""))
        
    def test_passwordall_true(self):
        '''
        Description:
            The given valid password returns true in this test case.
        '''
        self.assertTrue(Validation_User.validate_password("Ravadh@02"))
        self.assertTrue(Validation_User.validate_password("XHava+1234"))
        self.assertTrue(Validation_User.validate_password("AbcdEG12^4"))
        self.assertTrue(Validation_User.validate_password("vsgdhAR123%"))

    def test_passwordall_false(self):
        '''
        Description:
            The given invalid password returns false  in this test case.
        '''
        self.assertFalse(Validation_User.validate_password("1235799021"))
        self.assertFalse(Validation_User.validate_password("vbhyemusvvdbs"))
        self.assertFalse(Validation_User.validate_password("ARjunAKRISHN"))
        self.assertFalse(Validation_User.validate_password("Arj1&ux"))

if __name__ == '__main__':
    unittest.main()