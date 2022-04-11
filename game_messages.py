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
            responseMessage = self.game.checkAnswer(msg, clientAddress[0])
        elif typeMsg == constants.CHAT:
            responseMessage = self.game.chatMessage(msg, clientAddress[0])
        elif typeMsg == constants.TIMEOUT:
            responseMessage = self.game.timeoutMessage()
        elif typeMsg == constants.GAME_START and (clientAddress[0] == self.serverAddress or clientAddress[0] in constants.HOST_ADDRESS):
            self.sendMessageToAllPlayers(constants.GAME_START + '#' + constants.GAME_START)
            responseMessage = self.game.gameStartMessage()
        elif typeMsg == constants.ADD_PLAYER:
            responseMessage = self.game.addNewPlayer(msg, clientAddress)
        elif typeMsg == constants.REMOVE_PLAYER:
            responseMessage = self.game.removePlayer(clientAddress[0])
        else:
            responseMessage = (msg + '#' + constants.PRINT_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)
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
