'''
Created on 27 Jul, 2014

@author: feng
'''
from com.fengwangang.freechat.model import request
from com.fengwangang.freechat.model import response

import time

class Message():
    def __init__(self, sender=None, receiver=None, msg_type=None, content=None, send_time=None, receive_time=None):
        self.sender = sender
        self.receiver = receiver
        self.msg_type = msg_type
        self.content = content
        self.send_time = send_time
        self.receive_time = receive_time
        
    def json_format(self):
        json = dict()
        json['sender']=self.sender
        json['receiver']=self.receiver
        json['msg_type']=self.msg_type
        json['content']=self.content
        json['send_time']=self.send_time
        json['receive_time']=self.receive_time
        return json
        

class SendMessageRequest(request.BaseRequest):
    def __init__(self, uid, receiver, msg_type, content):
        super.__init__()
        self.receiver = receiver
        self.msg_type = msg_type
        self.content = content
        self.send_time = time.time()*1000
        

class SendMessageResponse(response.BaseResponse):
    def __init__(self):
        super.__init__()
        
class ReceiveMessageRequest(request.BaseRequest):
    def __init__(self, friend_id):
        super.__init__()
        self.friend_id = friend_id
        
class ReceiveMessageResponse(response.BaseResponse):
    def __init__(self, messages):
        super.__init__()
        self.messages = messages
        


