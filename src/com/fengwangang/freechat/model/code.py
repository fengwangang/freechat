'''
Created on 3 Aug, 2014

@author: feng
'''

class BaseCode:
    OK = 0
    SYSTEM_ERROR = -1

class LogInCode(BaseCode):
    INVALID_USER_NAME = 1
    INVALID_PASSWORD = 2
    USER_NOT_EXISTS = 3
    USER_PASSWORD_NOT_MATCH = 4
    