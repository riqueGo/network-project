from game import Game
import socket
import constants

class GameMessages:
    def __init__(self, serverAddress):
        self.game = Game(serverGameAddress = serverAddress)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddress = serverAddress

    def wichServerMessage(self, tupleMessage, clientAddress):
        tupleMessage = tupleMessage.split('#')
        msg = tupleMessage[0]
        typeMsg = tupleMessage[1]
        if typeMsg == constants.ANSWER:
            responseMessage = self.game.isCorrectAnswer(msg, clientAddress[0])
        elif typeMsg == constants.CHAT:
            responseMessage = (msg, constants.ALL_PLAYER_MESSAGE)
        elif typeMsg == constants.TIMEOUT:
            if msg == constants.WAITING_ROOM:
                self.sendMessageToAllPlayers(constants.GAME_STARTED)
                self.game.timer.start()
            else:
                self.game.timer.isRest = False
            responseMessage = self.game.startRound()
        elif typeMsg == constants.ADD_PLAYER:
            responseMessage = self.game.addNewPlayer(msg, clientAddress)
        elif typeMsg == constants.REMOVE_PLAYER:
            responseMessage = ((constants.DISCONNECTED_SERVER, constants.ALL_PLAYER_MESSAGE) if clientAddress[0] == self.serverAddress else self.game.removePlayer(clientAddress[0]))
        else:
            responseMessage = (msg, constants.SINGLE_PLAYER_MESSAGE)
        return responseMessage
    
    def sendMessage(self, message, clientAddress):
        msg = message[0]
        typeMsg = message[1]
        if(typeMsg == constants.SINGLE_PLAYER_MESSAGE):
            self.sendMessageToSinglePlayer(msg, clientAddress)
        else:
            self.sendMessageToAllPlayers(msg)
            
    def sendMessageToAllPlayers(self, message):
        players = self.game.listOfPlayers
        for ipAddress in players.keys():
            port = players.get(ipAddress).port
            self.sock.sendto(message.encode(), (ipAddress, port))
    
    def sendMessageToSinglePlayer(self, message, clientAddress):
        self.sock.sendto(message.encode(), clientAddress)
    