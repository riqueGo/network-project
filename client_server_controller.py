import socket
import constants
import help
from server import Server
from client import Client

serverGame = None

def createHostSession():
    #Server Starts
    s = Server()
    turnOnServer(s)
    s.start()

    #Instance of Client class
    host = Client()
    host.serverAddress = s.serverAddress
    host.startGame()

    #When host quits of game
    turnOffServer(s)
    help.menu()


def createSession():
    player = Client()
    player.startGame()
    help.menu()


def getLocalIp():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        return sock.getsockname()[0]
    except socket.error:
        try:
            return socket.gethostbyname(socket.gethostname())
        except socket.gaierror:
            return '127.0.0.1'
    finally:
        sock.close()


def turnOffServer(server):
    server.stopServer = True
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(constants.DISCONNECTED_SERVER.encode(), (server.serverAddress, constants.PORT))


def turnOnServer(server):
    global serverGame

    if serverGame == None:
        serverGame = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverGame.bind((server.serverAddress, constants.PORT))
    
    server.server = serverGame
    print('Servidor Iniciado\nEndereço: ' + server.serverAddress + '\n')
