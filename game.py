import constants
import random
import quiz
from player import ListOfPlayers
from timer import Timer

class Game:
    def __init__(self, serverGameIpAddress):
        self.players = ListOfPlayers()
        self.listQuiz = random.sample(quiz.listOfQuiz,constants.MAX_ROUNDS)
        self.answerOfCurrentRound = None
        self.timer = Timer(10, serverGameIpAddress)
        self.serverGameIpAddress = serverGameIpAddress
        self.gameOn = False

    
    def addNewPlayer(self, name, clientAddress):
        ipAddress = clientAddress[0]
        if self.gameOn:
            return (constants.GAME_RUNNING + '#' + constants.GAME_RUNNING, constants.SINGLE_PLAYER_MESSAGE)
        elif len(self.players.playersKeys()) < constants.MAX_PLAYERS and ipAddress not in self.players.playersKeys():
            self.players.addPlayer(name, clientAddress)
            return (self.players.listAllPlayers() + '#' + constants.ADD_PLAYER, constants.ALL_PLAYER_MESSAGE)
        elif len(self.players.playersKeys()) >= constants.MAX_PLAYERS and ipAddress not in self.players.playersKeys():
            return (constants.LOTATION_MESSAGE + '#' + constants.LOTATION_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)
        else:
            return ('You\'re already connected#' + constants.PRINT_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)

    
    def removePlayer(self, clientIpAddress):
        if (clientIpAddress == self.serverGameIpAddress or clientIpAddress in constants.HOST_ADDRESS):
            self.timer.turnOff()
            return (constants.DISCONNECTED_SERVER + '#' + constants.DISCONNECTED_SERVER, constants.ALL_PLAYER_MESSAGE) #If Host disconnect so disconnect all players
        name = self.players.removePlayer(clientIpAddress).name
        return (name + constants.REMOVE_PLAYER + '#' + constants.PRINT_MESSAGE, constants.ALL_PLAYER_MESSAGE)
    

    def startRound(self):
        message = self.players.scoreBoard() + '\n'
        try:
            roundGame = constants.MAX_ROUNDS - len(self.listQuiz) + 1
            quizTuple = self.listQuiz.pop()
            self.answerOfCurrentRound = quizTuple[1]
            message += 'Round ' + str(roundGame) + '\n'
            message += quizTuple[0] + '\n\n'
            message += '#' + constants.START_ROUND
            self.timer.count = 0
            self.players.removePointsFromNotAnsweredPlayers()
        except:
            self.timer.turnOff()
            message += '#' + constants.GAME_ENDED
        return message

    
    def checkAnswer(self, answer, clientIpAddress):
        player = self.players.getPlayer(clientIpAddress)
        player.answered = True
        if self.answerOfCurrentRound == answer:
            return (player.toScore() + '\n\n' + self.startRound(), constants.ALL_PLAYER_MESSAGE)
        return (player.loseScore() + '#' + constants.PRINT_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)

    def chatMessage(self, message, clientIpAddress):
        return (self.players.getPlayer(clientIpAddress).name + ': ' + message + '#' + constants.CHAT, constants.ALL_PLAYER_MESSAGE)
    
    def timeoutMessage(self):
        self.timer.isRest = False
        return (self.startRound(), constants.ALL_PLAYER_MESSAGE)
    
    def gameStartMessage(self):
        try:
            self.timer.start()
        except:
            self.timer.on = True
        return (self.startRound(), constants.ALL_PLAYER_MESSAGE)