from threading import Thread
import socket
import constants
import time


class Chat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.serverAddress = None
    
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            time.sleep(1)
            message = input('$: ')
            if message.upper() == constants.QUIT:
                sock.sendto(constants.REMOVE_PLAYER.encode(), (self.serverAddress, constants.PORT))
                break
            else:
                message += ' ' + constants.CHAT
                sock.sendto(message.encode(), (self.serverAddress, constants.PORT))