import socket
import constants
from threading import Thread
from game import Game
import help

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.game = Game()
        self.serverAddress = help.getLocalIp()
        self.server = None
        self.stopServer = False

    def run(self):
        self.server = self.createServer()
        while True:
            bytesMessage, clientAddress = self.server.recvfrom(2048)
            if self.stopServer:
                self.sendMessageToAllPlayers('Servidor desconectado')
                break
            message = self.wichMessage(bytesMessage.decode(), clientAddress)
            self.sendMessage(message, clientAddress)
        

    def createServer(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((self.serverAddress, constants.PORT))
        print('Server started')
        return server
    
    def wichMessage(self, message, clientAddress):
        if constants.ADD_PLAYER in message:
            message = message.replace(constants.ADD_PLAYER, '').strip()
            responseMessage = self.game.addNewPlayer(message, clientAddress)
        elif constants.REMOVE_PLAYER in message:
            responseMessage = ((constants.DISCONNECTED_SERVER, constants.ALL_PLAYER_MESSAGE) if clientAddress[0] == self.serverAddress else self.game.removePlayer(clientAddress[0]))
        elif constants.CHAT in message:
            message = message.replace(constants.CHAT, '').strip()
            responseMessage = (message, constants.ALL_PLAYER_MESSAGE)
        else:
            responseMessage = (message, constants.SINGLE_PLAYER_MESSAGE)
        return responseMessage
    
    def sendMessageToAllPlayers(self, message):
        players = self.game.listOfPlayers
        for ipAdress in players.keys():
            port = players.get(ipAdress).port
            self.server.sendto(message.encode(), (ipAdress, port))
    
    def sendMessageToSinglePlayer(self, message, clientAddress):
        self.server.sendto(message.encode(), clientAddress)
    
    def sendMessage(self, message, clientAddress):
        msg = message[0]
        typeMsg = message[1]
        if(typeMsg == constants.SINGLE_PLAYER_MESSAGE):
            self.sendMessageToSinglePlayer(msg, clientAddress)
        else:
            self.sendMessageToAllPlayers(msg)