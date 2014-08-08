'''
Created on 27 Jul, 2014

@author: feng
'''

import time

class BaseResponse:
    
    def __init__(self, ret=0):
        self.ret = ret
        self.response_time = time.time()*1000
