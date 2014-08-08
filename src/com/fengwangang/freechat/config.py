'''
Created on 27 Jul, 2014

@author: feng
'''

class GlobalConfig:
    STATIC_DIR = '../static'
    TEMPLATE_DIR = '../templates'
    SERVER_POST = 8080
    CHARSET = 'utf8'
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_NAME = 'freechat'
    DB_USER = 'root'
    DB_PASSWORD = 'feng'
    PASSWORD_SALT = 'Fr2eCh@'
    DEFAULT_AVATAR = '/static/avatars/avatar.png'
    def reload(self):
        print('reload config')
                

    
