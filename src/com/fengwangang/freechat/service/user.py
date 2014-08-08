'''
Created on 27 Jul, 2014

@author: feng
'''
import pymysql

from com.fengwangang.freechat.config import GlobalConfig
from com.fengwangang.freechat.model.user import User
from com.fengwangang.freechat.model.user import Friend

class UserService:
    
    @staticmethod
    def get_user_by_account(account):
        if None == account:
            return None
        conn = pymysql.connect(host=GlobalConfig.DB_HOST, port=GlobalConfig.DB_PORT, user=GlobalConfig.DB_USER, passwd=GlobalConfig.DB_PASSWORD, db=GlobalConfig.DB_NAME, charset=GlobalConfig.CHARSET)
        sql = 'SELECT uid,name,password,avatar,emotion,token FROM user WHERE uid = %d' % int(account)
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            for c in cursor:
                uid = c[0]
                name = c[1]
                password = c[2]
                avatar = c[3]
                if None == avatar:
                    avatar = GlobalConfig.DEFAULT_AVATAR
                emotion = c[4]
                token = c[5]
                user = User(uid=uid, name=name, password=password,avatar=avatar,emotion=emotion,token=token)
                return user
        except IOError as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return None
    
class FriendService:
    
    @staticmethod
    def get_friends(uid):
        if None == uid:
            return None
        conn = pymysql.connect(host=GlobalConfig.DB_HOST, port=GlobalConfig.DB_PORT, user=GlobalConfig.DB_USER, passwd=GlobalConfig.DB_PASSWORD, db=GlobalConfig.DB_NAME, charset=GlobalConfig.CHARSET)
        sql = 'SELECT f.friend_id,f.alias_name,u.name,u.avatar,u.emotion,u.status FROM friendship f JOIN user u ON f.friend_id=u.uid WHERE f.uid=%d AND f.is_deleted=0' 
        cursor = conn.cursor()
        try:
            cursor.execute(sql % int(uid))
            friends=[]
            for c in cursor:
                friend_id = c[0]
                alias_name = c[1]
                name = c[2]
                if None == alias_name:
                    alias_name = name
                    if None == alias_name:
                        alias_name = friend_id
                avatar = c[3]
                if None == avatar:
                    avatar = GlobalConfig.DEFAULT_AVATAR
                emotion = c[4]
                status = c[5]
                friend = Friend(friend_id=friend_id,alias_name=alias_name,status=status,emotion=emotion,avatar=avatar)
                friends.append(friend)
            return friends
        except IOError as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return None
