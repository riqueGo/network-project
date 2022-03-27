import socket
import time
import constants
import help
from threading import Thread

class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddress = None

    def run(self):
        while True:
            bytesMessage, serverAddress = self.client.recvfrom(2048)
            msg = bytesMessage.decode()
            
            if msg == constants.LOTATION_MESSAGE:
                break
            elif constants.JOINNED_PLAYER in msg:
                print(msg.replace(constants.JOINNED_PLAYER, '').strip())
            elif constants.REMOVE_PLAYER in msg:
                print('Você saiu do Jogo')
                break
            elif msg == constants.DISCONNECTED_SERVER:
                print(constants.DISCONNECTED_SERVER)
                break
            else:
                print(msg)
            
    
    def joinTheGame(self):
        name = input('Digite seu nickname: ')
        name += ' ' + constants.ADD_PLAYER
        self.client.sendto(name.encode(),(self.serverAddress,constants.PORT))
                