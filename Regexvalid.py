'''
@Author: Rashmi
@Date: 2021-09-28 23:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 1:35
@Title :Write a Python program test cases for user registration'''
import re
from LoggerHandler import logger

class Validation_User():

    def validate_name(name):
        '''
        Description:
            To check the given first and last name where name starts with capital letter 
            and should have minimum three characters.
        Parameters:
            name--->for firstname,lastname
        Return:
            boolean value
        '''      
        try:
            return bool(re.match("^[A-Z]{1}[a-z]{2,}$", name))
        except Exception as e:
            logger.error(e)
    
    def validate_email(email):
        '''
        Description:
            E.g. abc.xyz@bl.co.in - Email has 3 mandatory parts (abc, bl & co) and 2 optional
             (xyz & in) with precise @ and . positions
        Parameters:
            email : email to validate
        Return:
            boolean value
        '''        
        try:
            return bool(re.match(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email))
        except Exception as e:
            logger.error(e)
    
    def validate_phone_number(number):
        '''
        Description:
                E.g. 91 9919819801 - Country code(91) follow by space and 10 digit
                number(starting with 8/9)
        Parameters:
            number: phone number to validate
        Return:
            boolean value
        '''        
        try:
            return bool(re.match("^[9]{1}[1]{1}\\s[8-9]{1}[0-9]{9}$", number))
        except Exception as e:
            logger.error(e)
    
    def validate_password(passwd):
        '''
        Description:
                As a User need to follow pre-defined Password rules. 
                Rule3– minimum 8 Characters min 1 upper case 1 numerical number
                and atleast 1 special character
                NOTE – All rules must be passed
        Parameters:
            passwd: password to validate
        Returns:
            boolean 
        '''        
        try:
            return bool(re.match("^(?=.*[@#$%^&+=])(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}$", passwd))
        except Exception as e:
            logger.error(e)
