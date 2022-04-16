from game import Game
import socket
import constants

class GameMessages:
    def __init__(self, serverIpAddress):
        self.game = Game(serverGameIpAddress = serverIpAddress)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
        elif typeMsg == constants.GAME_START and (clientAddress[0] == self.serverIpAddress or clientAddress[0] in constants.HOST_ADDRESS):
            if self.game.gameOn == False:
                self.sendMessageToAllPlayers(constants.GAME_START + '#' + constants.GAME_START)
            responseMessage = self.game.gameStartMessage()
        elif typeMsg == constants.ADD_PLAYER:
            responseMessage = self.game.addNewPlayer(msg, clientAddress)
        elif typeMsg == constants.REMOVE_PLAYER:
            if (clientAddress[0] == self.serverIpAddress or clientAddress[0] in constants.HOST_ADDRESS):
                responseMessage = self.game.removeHostPlayer()
            else:
                responseMessage = self.game.removePlayer(clientAddress[0])
                self.sendMessageToSinglePlayer(constants.REMOVE_PLAYER + '#' + constants.REMOVE_PLAYER, clientAddress)
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
            self.sock.sendto(message.encode(), (playerIpAddress, port))
    
    def sendMessageToSinglePlayer(self, message, clientAddress):
        self.sock.sendto(message.encode(), clientAddress)
