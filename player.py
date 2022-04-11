import constants

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.port = None
    
    def toScore(self):
        self.score += constants.TO_SCORE
        return self.name + ' ' + constants.CORRECT_ANSWER
    
    def loseScore(self):
        self.score -= constants.LOSE_SCORE
        return constants.WRONG_ANSWER