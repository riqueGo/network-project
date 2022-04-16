from threading import Thread
import constants
import help


class Chat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.serverAddress = None
        self.clientSocket = None
        self.isChatOn = True
        self.isGameOn = False
        self.isChatAlive = True
    
    def run(self):
        while self.isChatAlive:
            message = input()
            if message.upper() == constants.QUIT:
                message = constants.REMOVE_PLAYER + '#' + constants.REMOVE_PLAYER
            elif message.upper() == constants.START_COMMAND:
                message += '#' + constants.GAME_START
            elif message.upper() == constants.CONNECTED_PLAYERS:
                message += '#' + constants.CONNECTED_PLAYERS
            elif message.upper() == constants.HELP:
                help.commandsList()
                continue
            elif self.isGameOn:
                message += '#' + constants.ANSWER
            elif self.isChatOn:
                message += '#' + constants.CHAT
            else:
                print('Não é possível enviar mensagem no momento')
                continue
            if self.isChatAlive:
                self.clientSocket.sendto(message.encode(), (self.serverAddress, constants.PORT))