'''
Created on 3 Aug, 2014

@author: feng
'''
import re
import hashlib
from com.fengwangang.freechat.config import GlobalConfig
import uuid

class UserUtil:
    
    @staticmethod
    def check_username(username):
        if None == username or not username.strip():
            return False
        else:
            if username.isnumeric():
                return True
            else:
                email_reg = r'^(\w)+(_)*(\w)+@(\w)+(\.)(\S)+$'
                email_pattern = re.compile(email_reg)
                if email_pattern.match(username):
                    return True
            return False
        
    @staticmethod
    def check_password(password):
        if None == password or not password.strip():
            return False
        else:
            return len(password) >=6 and len(password) <=32
    
    @staticmethod
    def encrypt_password(password):
        if None == password or not password.strip():
            return None
        else:
            return hashlib.md5(password.join(GlobalConfig.PASSWORD_SALT).encode(GlobalConfig.CHARSET)).hexdigest().upper()
    
    @staticmethod
    def gen_token():
        return hashlib.md5(str(uuid.uuid4()).encode(GlobalConfig.CHARSET)).hexdigest().upper()    
    
