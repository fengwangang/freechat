'''
Created on 27 Jul, 2014

@author: feng
'''

class User:
    def __init__(self,uid, name, password, gender=0, avatar=None, status=0, emotion=None, token=None):
        self.uid = uid
        self.name = name
        self.password = password
        self.gender = gender
        self.avatar = avatar
        self.status = status
        self.emotion = emotion
        self.token = token
        

class Friend:
    def __init__(self, friend_id, alias_name=None, status=None, emotion=None, avatar=None):
        self.friend_id = friend_id
        self.alias_name = alias_name
        self.status = status
        self.emotion = emotion
        self.avatar = avatar


        
