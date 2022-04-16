import socket
import time
import client_server_controller
from chat import Chat
import constants
from threading import Thread
import help

class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientAddress = client_server_controller.getLocalIp()
        self.serverAddress = None
        self.breakMessages = [constants.REMOVE_PLAYER, constants.DISCONNECTED_SERVER]
        self.clientOn = True
        self.name = None
        self.chat = Chat()

    def run(self):
        self.client.settimeout(20)
        while self.clientOn:
            try:
                bytesMessage, serverAddress = self.client.recvfrom(2048)
                message = bytesMessage.decode()
            except:
                message = ('Sem resposta do servidor#' + constants.TIMEOUT)
            self.wichClientMessage(message)
    
    def wichClientMessage(self, responseMessage):
        tupleMessage = responseMessage.split('#')
        msg = tupleMessage[0]
        typeMsg = tupleMessage[1]

        if typeMsg in self.breakMessages:
            if typeMsg == constants.DISCONNECTED_SERVER and not help.isHost(self.clientAddress, self.serverAddress):
                print(msg)
            print('Você saiu da sala, pressione enter para voltar ao menu principal')
            self.chat.isChatAlive = False
            self.clientOn = False
        elif typeMsg == constants.GAME_START:
            print('Chat Fechado. Bom jogo!\n\n')
            self.chat.isChatOn = False
            self.chat.isGameOn = True
            print(msg + '\n') 
        elif typeMsg == constants.GAME_ENDED:
            self.chat.isChatOn = True
            self.chat.isGameOn = False
            print(typeMsg + '\nPlacar final')
            print(msg + '\n')
            print('Chat Aberto\nPara sair da sala digite \'/quit\'') 
        elif typeMsg == constants.LOTATION_MESSAGE or typeMsg == constants.GAME_RUNNING:
            self.notPossibleToJoinRoom(typeMsg)
        else:
            print(msg + '\n') 
    
    def joinPlayer(self):
        self.name = input('Digite seu nickname: ')
    
    def joinGameRoom(self):
        player = self.name + '#' + constants.ADD_PLAYER
        try:
            self.client.sendto(player.encode(),(self.serverAddress,constants.PORT))
            self.client.settimeout(2)
            bytesMessage, serverAddress = self.client.recvfrom(2048)
            self.client.settimeout(None)
            self.wichClientMessage(bytesMessage.decode())
        except:
            self.notPossibleToJoinRoom(constants.INVALID_ADDRESS)
    
    def startChat(self):
        self.chat.serverAddress = self.serverAddress
        self.chat.clientSocket = self.client
        self.chat.start()
    
    def startGame(self):
        self.joinPlayer()
        self.getServerAddress()
        self.joinGameRoom()
        if self.clientOn:
            help.commandsList()
            self.startChat()
            self.start()
            self.chat.join()
    
    def getServerAddress(self):
        if (not help.isHost(self.clientAddress, self.serverAddress)):
            self.serverAddress = input('Digite endereço da partida: ') #If client is not a Host
            print()
    
    def notPossibleToJoinRoom(self, motive):
        self.clientOn = False
        print('Não foi possível entrar na sala, ' + motive + '\n')

                