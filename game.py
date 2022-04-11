import constants
import random
import quiz
from player import Player
from timer import Timer

class Game:
    def __init__(self, serverGameAddress):
        self.listOfPlayers = dict()
        self.listQuiz = random.sample(quiz.listOfQuiz,constants.MAX_ROUNDS)
        self.answerOfCurrentRound = None
        self.timer = Timer(10, serverGameAddress)
        self.serverGameAddress = serverGameAddress

    
    def addNewPlayer(self, name, clientAddress):
        ipAddress = clientAddress[0]
        if len(self.listOfPlayers.keys()) < constants.MAX_PLAYERS and ipAddress not in self.listOfPlayers.keys():
            p = Player(name)
            p.port = clientAddress[1]
            self.listOfPlayers[ipAddress] = p
            return (self.listAllPlayers() + '#' + constants.ADD_PLAYER, constants.ALL_PLAYER_MESSAGE)
        elif len(self.listOfPlayers.keys()) >= constants.MAX_PLAYERS and ipAddress not in self.listOfPlayers.keys():
            return (constants.LOTATION_MESSAGE + '#' + constants.LOTATION_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)
        else:
            return ('You\'re already connected#' + constants.PRINT_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)

    
    def removePlayer(self, clientAddress):
        if (clientAddress == self.serverGameAddress or clientAddress in constants.HOST_ADDRESS):
            self.timer.turnOff()
            return (constants.DISCONNECTED_SERVER + '#' + constants.DISCONNECTED_SERVER, constants.ALL_PLAYER_MESSAGE) #If Host disconnect so disconnect all players
        name = self.listOfPlayers.get(clientAddress).Name
        self.listOfPlayers.pop(clientAddress)
        return (str(name) + constants.REMOVE_PLAYER + '#' + constants.PRINT_MESSAGE, constants.ALL_PLAYER_MESSAGE)
    
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
            message += '#' + constants.START_ROUND
            self.timer.count = 0
        except:
            self.timer.turnOff()
            message += '#' + constants.GAME_ENDED
        return message

    
    def checkAnswer(self, answer, clientAddress):
        player = self.listOfPlayers.get(clientAddress)
        if self.answerOfCurrentRound == answer:
            return (player.toScore() + '\n\n' + self.startRound(), constants.ALL_PLAYER_MESSAGE)
        return (player.loseScore() + '#' + constants.PRINT_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)

    def chatMessage(self, message, clientAddress):
        return (self.listOfPlayers.get(clientAddress).name + ': ' + message + '#' + constants.CHAT, constants.ALL_PLAYER_MESSAGE)
    
    def timeoutMessage(self):
        self.timer.isRest = False
        return (self.startRound(), constants.ALL_PLAYER_MESSAGE)
    
    def gameStartMessage(self):
        try:
            self.timer.start()
        except:
            self.timer.on = True
        return (self.startRound(), constants.ALL_PLAYER_MESSAGE)