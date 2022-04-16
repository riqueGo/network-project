from game import Game
import socket
import constants
import help

class GameMessages:
    def __init__(self, serverIpAddress, serverSocket):
        self.game = Game(serverGameIpAddress = serverIpAddress)
        self.serverSocket = serverSocket
        self.serverIpAddress = serverIpAddress

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
        elif typeMsg == constants.GAME_START:
            responseMessage = self.gameStartMessageValidation(clientAddress[0])
        elif typeMsg == constants.ADD_PLAYER:
            responseMessage = self.game.addNewPlayer(msg, clientAddress)
        elif typeMsg == constants.REMOVE_PLAYER:
            responseMessage = self.removePlayerMessageValidation(clientAddress)
        elif typeMsg == constants.CONNECTED_PLAYERS:
            responseMessage = self.game.connectedPlayersMessage()
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
        players = self.game.players
        for playerIpAddress in players.playersKeys():
            port = players.getPlayer(playerIpAddress).port
            self.serverSocket.sendto(message.encode(), (playerIpAddress, port))
    
    def sendMessageToSinglePlayer(self, message, clientAddress):
        self.serverSocket.sendto(message.encode(), clientAddress)
    
    def gameStartMessageValidation(self, clientIpAddress):
        if (help.isHost(clientIpAddress, self.serverIpAddress)):
            if self.game.gameOn == False:
                self.sendMessageToAllPlayers(constants.GAME_START + '#' + constants.GAME_START)
            return self.game.gameStartMessage()
        else:
            return ('Apenas o Host pode iniciar a partida#' + constants.PRINT_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)
    
    def removePlayerMessageValidation(self, clientAddress):
        if (help.isHost(clientAddress[0], self.serverIpAddress)):
            return self.game.removeHostPlayer()
        else:
            self.sendMessageToSinglePlayer(constants.REMOVE_PLAYER + '#' + constants.REMOVE_PLAYER, clientAddress)
            return self.game.removePlayer(clientAddress[0])