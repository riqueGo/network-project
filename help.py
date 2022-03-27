import socket
import time
import constants
from server import Server
from client import Client

def menu():
    while True:
        choice = input('Bem vindo ao Quiz Game\n' +
        'Escolha uma opção de acordo com o número abaixo:\n\n' +
        '1 - Criar Partida\n' +
        '2 - Entrar em uma partida\n\n')

        if choice == '1':
            createSession()
            break
        elif choice == '2':
            #TODO Client
            break
        else:
            print('Escolha uma opção válida: (\'1\' ou \'2\')\n\n')

def createSession():
    s = Server()
    s.start()
    time.sleep(1)
    c = Client()
    c.serverAddress = s.serverAddress
    c.start()
    chat(s.serverAddress)
    turnOffServer(s)

    

def getLocalIp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]
    except socket.error:
        try:
            return socket.gethostbyname(socket.gethostname())
        except socket.gaierror:
            return '127.0.0.1'
    finally:
        s.close()

def turnOffServer(server):
    server.stopServer = True
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(constants.DISCONNECTED_SERVER.encode(), (server.serverAddress, constants.PORT))

def chat(serverAddress):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        time.sleep(2)
        message = input('$: ')
        if message.upper() == constants.QUIT:
            s.sendto(constants.REMOVE_PLAYER.encode(), (serverAddress, constants.PORT))
            break
        else:
            message += ' ' + constants.CHAT
            s.sendto(message.encode(), (serverAddress, constants.PORT))





