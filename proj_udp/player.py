import constants

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.port = None
        self.answered = True
    
    def toScore(self):
        self.score += constants.TO_SCORE
        return self.name + ' ' + constants.CORRECT_ANSWER
    
    def loseScore(self):
        self.score -= constants.LOSE_SCORE
        return constants.WRONG_ANSWER

class ListOfPlayers:
    def __init__(self):
        self.listOfPlayers = dict()
    
    def getPlayer(self, clientIpAddress):
        return self.listOfPlayers.get(clientIpAddress)
    
    def addPlayer(self, name, clientAddress):
        p = Player(name)
        p.port = clientAddress[1]
        self.listOfPlayers[clientAddress[0]] = p
    
    def removePlayer(self, index):
        return self.listOfPlayers.pop(index)
    
    def listAllPlayers(self):
        allPlayers = '================================================================\n'
        for p in self.listOfPlayers.values():
            allPlayers += p.name + '    connected\n'
        allPlayers += '================================================================\n\n'
        return allPlayers
    
    def scoreBoard(self):
        sortedPlayerList = sorted(self.listOfPlayers.values(), key=lambda p: p.score, reverse=True)
        allPlayers = '================================================================\n'
        for i, p in enumerate (sortedPlayerList):
            allPlayers += str(i+1) + ' ' + p.name + '    ' + str(p.score) + ' pontos\n'
        allPlayers += '================================================================\n\n'
        return allPlayers
    
    def playersKeys(self):
        return self.listOfPlayers.keys()
    
    def removePointsFromNotAnsweredPlayers(self):
        for p in self.listOfPlayers.values():
            if p.answered == False:
                p.score -= constants.NO_SCORE
            p.answered = False

    def resetListPlayers(self):
        for p in self.listOfPlayers.values():
            p.score = 0
            p.answered = True