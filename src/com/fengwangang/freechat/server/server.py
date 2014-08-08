'''
Created on 27 Jul, 2014

@author: feng
'''
connections = dict()
class FreechatServer:
    
    @staticmethod
    def register(uid, callback):
        connections[uid] = callback
        
    @staticmethod
    def receive(message):
        if FreechatServer.push(message):
            pass
        else:
            FreechatServer.store(message)
    
    @staticmethod
    def push(message):
        receiver = message.receiver
        if FreechatServer.check_online_user(receiver):
            connection = connections[receiver]
            connection(message)
            return True
        else:
            return False
        
    @staticmethod
    def store(message):
        print('store message into db...')
    
    @staticmethod
    def log_out(uid, connection):
        del connections[uid]
    
    @staticmethod
    def check_online_user(uid):
        if uid in connections.keys():
            return True
        else:
            return False

        
    
            
    