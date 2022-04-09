import socket
import constants
from threading import Thread
from game_messages import GameMessages
import clinet_server_controller

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.serverAddress = clinet_server_controller.getLocalIp()
        self.server = None
        self.stopServer = False

    def run(self):
        self.server = self.createServer()
        game = GameMessages(serverAddress = self.serverAddress)
        while True:
            bytesMessage, clientAddress = self.server.recvfrom(2048)
            if self.stopServer:
                game.sendMessageToAllPlayers(constants.DISCONNECTED_SERVER)
                break
            message = game.wichServerMessage(bytesMessage.decode(), clientAddress)
            game.sendMessage(message, clientAddress)
        

    def createServer(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((self.serverAddress, constants.PORT))
        print('Servidor Iniciado\nEndereço: ' + self.serverAddress + '\n')
        return server