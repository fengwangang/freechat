'''
Created on 27 Jul, 2014

@author: feng
'''

import tornado.web

from com.fengwangang.freechat.utils import UserUtil
from com.fengwangang.freechat.service.user import UserService
from com.fengwangang.freechat.service.user import FriendService
from com.fengwangang.freechat.server.auth import AuthHandler

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', account = '', error = '')

class LogInHandler(tornado.web.RequestHandler):
    def post(self):
        account = self.get_argument('account', None)
        password = self.get_argument('password', None)
        if not UserUtil.check_username(account):
            self.render('index.html', account=account, error='Invalid Account')
        elif not UserUtil.check_password(password):
            self.render('index.html', account=account, error='Invalid Password')
        user = UserService.get_user_by_account(account)
        if None == user:
            self.render('index.html', account='', error='Account Not Exist')
        db_password = user.password
        encrypt_password = UserUtil.encrypt_password(password)
        if db_password != encrypt_password:
            self.render('index.html', account=account, error='Account/Password Not Match')
        friends = FriendService.get_friends(account)
        self.set_cookie('uid', str(user.uid))
        self.set_cookie('token', user.token)
        AuthHandler.update_auth(int(user.uid), user.token)
        self.render('chat.html', user=user, friends=friends)
        
