'''
Created on 27 Jul, 2014

@author: feng
'''

import time

class BaseRequest():
    
    def __init__(self, uid, token):
        self.uid = uid
        self.token = token
        self.request_time = time.time()*1000
