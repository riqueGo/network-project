from threading import Thread
import socket
import constants
import time


class Chat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.serverAddress = None
        self.clientSocket = None
        self.isChatAlive = True
        self.isGameOn = False
    
    def run(self):
        while True:
            message = input()
            if message.upper() == constants.QUIT:
                msg = constants.REMOVE_PLAYER + '#' + constants.REMOVE_PLAYER
                self.clientSocket.sendto(msg.encode(), (self.serverAddress, constants.PORT))
                self.clientSocket.sendto(msg.encode(), self.clientSocket.getsockname())
                break
            elif message.upper() == constants.START_COMMAND:
                message += '#' + constants.GAME_START
            elif self.isGameOn:
                message += '#' + constants.ANSWER
            elif self.isChatAlive:
                message += '#' + constants.CHAT
            else:
                print('Não é possível enviar mensagem no momento')
                continue
            self.clientSocket.sendto(message.encode(), (self.serverAddress, constants.PORT))