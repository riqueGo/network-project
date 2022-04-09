import constants
import random
import quiz
import clinet_server_controller
from player import Player
from timer import Timer

class Game:
    def __init__(self, serverGameAddress):
        self.listOfPlayers = dict()
        self.listQuiz = random.sample(quiz.listOfQuiz,constants.MAX_ROUNDS)
        self.answerOfCurrentRound = None
        self.timer = Timer(constants.GAME_STARTED, 3, serverGameAddress)

    
    def addNewPlayer(self, name, clientAddress):
        maxPlayer = 5
        ipAddress = clientAddress[0]
        if len(self.listOfPlayers.keys()) < maxPlayer and ipAddress not in self.listOfPlayers.keys():
            p = Player(name)
            p.port = clientAddress[1]
            self.listOfPlayers[ipAddress] = p
            return (self.listAllPlayers(), constants.ALL_PLAYER_MESSAGE)
        elif len(self.listOfPlayers.keys()) >= maxPlayer and ipAddress not in self.listOfPlayers.keys():
            return (constants.LOTATION_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)
        else:
            return ('You\'re already connected', constants.SINGLE_PLAYER_MESSAGE)

    def removePlayer(self, ipAddress):
        name = self.listOfPlayers.get(ipAddress)
        self.listOfPlayers.pop(ipAddress)
        return (str(name) + ' foi desconectado', constants.ALL_PLAYER_MESSAGE)
    
    def scoreBoard(self):
        allPlayers = '================================================================\n'
        for p in self.listOfPlayers.values():
            allPlayers += p.name + '    ' + str(p.score) + ' pontos\n'
        allPlayers += '================================================================\n\n'
        return allPlayers
    
    def listAllPlayers(self):
        allPlayers = '================================================================\n'
        for p in self.listOfPlayers.values():
            allPlayers += p.name + '    connected\n'
        allPlayers += '================================================================\n\n'
        return allPlayers
    
    def startRound(self):
        message = self.scoreBoard() + '\n'
        try:
            roundGame = constants.MAX_ROUNDS - len(self.listQuiz) + 1
            quizTuple = self.listQuiz.pop()
            self.answerOfCurrentRound = quizTuple[1]
            message += 'Round ' + str(roundGame) + '\n'
            message += quizTuple[0] + '\n\n'
            self.timer.count = 0
        except:
            self.timer.isRest = False
            self.timer.on = False
            message = constants.GAME_ENDED
        return (message, constants.ALL_PLAYER_MESSAGE)
    
    def isCorrectAnswer(self, answer, clientAddress):
        if self.answerOfCurrentRound == answer:
            self.listOfPlayers.get(clientAddress).score += 25
            return self.startRound()
        else:
            self.listOfPlayers.get(clientAddress).score -= 5
            return ('Você errou!', constants.SINGLE_PLAYER_MESSAGE)