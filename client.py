import socket
import time
from chat import Chat
import constants
from threading import Thread

class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddress = None
        self.breakMessages = [constants.LOTATION_MESSAGE, constants.REMOVE_PLAYER, constants.DISCONNECTED_SERVER, constants.GAME_ENDED]

    def run(self):
        chat = Chat()
        chat.serverAddress = self.serverAddress
        chat.clientAddress = self.client.getsockname()
        chat.start()
        while True:
            bytesMessage, serverAddress = self.client.recvfrom(2048)
            msg = bytesMessage.decode()
            if msg in self.breakMessages:
                print(msg)
                break
            elif msg == constants.GAME_STARTED:
                chat.isChatAlive = False
                chat.isGameOn = True
            else:
                print(msg)
            
            
    
    def joinPlayer(self):
        time.sleep(1)
        name = input('Digite seu nickname: ')
        name += '#' + constants.ADD_PLAYER
        self.client.sendto(name.encode(),(self.serverAddress,constants.PORT))
    
    def joinTheGame(self):
        time.sleep(1)
        address = input('Digite endereço da partida: ')
        self.serverAddress = address
                