'''
Created on 27 Jul, 2014

@author: feng
'''
import tornado.web
import tornado.ioloop
import tornado.httpserver

from com.fengwangang.freechat.config import GlobalConfig
from com.fengwangang.freechat.handler import user
from com.fengwangang.freechat.handler import message

import os

def main():
    application = tornado.web.Application(
        [
            (r'/', user.IndexHandler),
            (r'/login', user.LogInHandler),
            (r'/pull', message.ReceiveMessageHandler),
            (r'/send', message.SendMessageHandler)
        ],
        template_path = os.path.join(os.path.dirname(__file__),GlobalConfig.TEMPLATE_DIR),
        static_path = os.path.join(os.path.dirname(__file__),GlobalConfig.STATIC_DIR) 
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(GlobalConfig.SERVER_POST)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    print('starting server...')
    main()
    
