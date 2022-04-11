import socket
import constants
from threading import Thread
from game_messages import GameMessages
import client_server_controller

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.serverAddress = client_server_controller.getLocalIp()
        self.server = None
        self.stopServer = False


    def run(self):
        game = GameMessages(serverAddress = self.serverAddress)
        while True:
            bytesMessage, clientAddress = self.server.recvfrom(2048)
            if self.stopServer:
                game.sendMessageToAllPlayers(constants.DISCONNECTED_SERVER + '#' + constants.DISCONNECTED_SERVER)
                break
            message = game.wichServerMessage(bytesMessage.decode(), clientAddress)
            game.sendMessage(message, clientAddress)
        