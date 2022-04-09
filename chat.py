from threading import Thread
import socket
import constants
import time


class Chat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.serverAddress = None
        self.clientAddress = None
        self.isChatAlive = True
        self.isGameOn = False
    
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            message = input()
            if message.upper() == constants.QUIT:
                sock.sendto(constants.REMOVE_PLAYER.encode(), (self.serverAddress, constants.PORT))
                sock.sendto(constants.REMOVE_PLAYER.encode(), self.clientAddress)
                break
            elif self.isChatAlive:
                message += '#' + constants.CHAT
                sock.sendto(message.encode(), (self.serverAddress, constants.PORT))
            elif self.isGameOn:
                message += '#' + constants.ANSWER
                sock.sendto(message.encode(), (self.serverAddress, constants.PORT))
            else:
                print('Não é possível enviar mensagem no momento')