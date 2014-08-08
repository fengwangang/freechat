'''
Created on 27 Jul, 2014

@author: feng
'''

import tornado.web

from com.fengwangang.freechat.server.server import FreechatServer
from com.fengwangang.freechat.server.auth import AuthHandler
from com.fengwangang.freechat.model.response import BaseResponse
from com.fengwangang.freechat.model.message import Message

class SendMessageHandler(tornado.web.RequestHandler):
    def post(self):
        sender = int(self.get_argument("sender", 0))
        receiver = int(self.get_argument("receiver", 0))
        msg_type = int(self.get_argument("msg_type", 0))
        content = self.get_argument("msg_content", '')
        #send_message_request = message.SendMessageRequest(uid=sender, receiver=receiver, msg_type=msg_type, content=content)
        message = Message(sender=sender, receiver=receiver, msg_type=msg_type,content=content)
        FreechatServer.receive(message)
        
class ReceiveMessageHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        response = BaseResponse()
        uid_str = self.get_argument('uid', None)
        token = self.get_argument('token', None)
        if None == uid_str or None == token:
            response.ret = -1
            self.close_connection(dict(response))
        uid = int(uid_str)
        if AuthHandler.do_auth(uid, token):        
            FreechatServer.register(uid=uid, callback = self.push_messages)
        else:
            self.close_connection({'auth':False})

    def push_messages(self, response):
        if self.request.connection.stream.closed():
            return
        self.finish(response.json_format())
        
    def close_connection(self, response):
        self.finish(dict(response))
        
        
        
