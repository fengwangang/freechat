'''
Created on 27 Jul, 2014

@author: feng
'''
auth_keys=dict()

class AuthHandler:
    
    @staticmethod
    def update_auth(uid, token):
        if None == uid or None == token:
            print('update auth failed.uid:%s,token:%s' % (uid, token))
        else:
            auth_keys[uid] = token
      
    @staticmethod      
    def do_auth(uid, token):
        user_token = auth_keys.get(uid , None)
        if None == user_token or user_token != token:
            print('auth failed.uid:%s,token:%s' % (uid, token))
            return False
        else:
            return True 
            