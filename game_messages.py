from pexpect import TIMEOUT
from game import Game
import socket
import constants
import quiz
import random

class GameMessages:
    def __init__(self):
        self.game = Game()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddress = None
    
    def wichMessage(self, message, clientAddress):
        if constants.ADD_PLAYER in message:
            message = message.replace(constants.ADD_PLAYER, '').strip()
            responseMessage = self.game.addNewPlayer(message, clientAddress)
        elif constants.REMOVE_PLAYER in message:
            responseMessage = ((constants.DISCONNECTED_SERVER, constants.ALL_PLAYER_MESSAGE) if clientAddress[0] == self.serverAddress else self.game.removePlayer(clientAddress[0]))
        elif constants.CHAT in message:
            message = message.replace(constants.CHAT, '').strip()
            responseMessage = (message, constants.ALL_PLAYER_MESSAGE)
        elif constants.TIMEOUT in message:
            message = constants.START_ROUND
            responseMessage = (message, constants.ALL_PLAYER_MESSAGE)
        else:
            responseMessage = (message, constants.SINGLE_PLAYER_MESSAGE)
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
        for ipAdress in players.keys():
            port = players.get(ipAdress).port
            self.sock.sendto(message.encode(), (ipAdress, port))
    
    def sendMessageToSinglePlayer(self, message, clientAddress):
        self.sock.sendto(message.encode(), clientAddress)
    
    def createQuizList(self):
        self.game.listQuiz = random.sample(quiz.listOfQuiz,5)