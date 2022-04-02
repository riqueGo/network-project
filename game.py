import constants
from player import Player

class Game:
    def __init__(self):
        self.listOfPlayers = dict()
        self.listQuiz = None
    
    def addNewPlayer(self, name, clientAddress):
        maxPlayer = 5
        ipAddress = clientAddress[0]
        if len(self.listOfPlayers.keys()) < maxPlayer and ipAddress not in self.listOfPlayers.keys():
            message = (name + ' joined the game ' + constants.JOINNED_PLAYER, constants.ALL_PLAYER_MESSAGE)
            p = Player(name)
            p.port = clientAddress[1]
            self.listOfPlayers[ipAddress] = p
            return message
        elif len(self.listOfPlayers.keys()) >= maxPlayer and ipAddress not in self.listOfPlayers.keys():
            return (constants.LOTATION_MESSAGE, constants.SINGLE_PLAYER_MESSAGE)
        else:
            return ('You\'re already connected', constants.SINGLE_PLAYER_MESSAGE)

    def removePlayer(self, ipAddress):
        name = self.listOfPlayers.get(ipAddress)
        self.listOfPlayers.pop(ipAddress)
        return (str(name) + ' was disconected', constants.ALL_PLAYER_MESSAGE)