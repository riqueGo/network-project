import socket
import time
import constants
from server import Server
from client import Client
from chat import Chat

def createHostSession():
    s = Server()
    s.start()
    time.sleep(1)
    host = Client()
    host.serverAddress = s.serverAddress
    host.joinPlayer()
    host.start()
    #time.sleep(1)
    #turnOffServer(s)

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

def chat(serverAddress):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        time.sleep(1)
        message = input('$: ')
        if message.upper() == constants.QUIT:
            sock.sendto(constants.REMOVE_PLAYER.encode(), (serverAddress, constants.PORT))
            break
        else:
            message += ' ' + constants.CHAT
            sock.sendto(message.encode(), (serverAddress, constants.PORT))

def roundControl(clientPlayer):
    while True:
        clientPlayer.start()
        time.sleep(1)
        c = Chat()
        c.serverAddress = clientPlayer.ServerAddress
        c.start()
        chat(clientPlayer.serverAddress)

def createSession():
    player = Client()
    player.joinTheGame()
    player.joinPlayer()
    c = Chat()
    c.serverAddress = player.serverAddress
    c.start()

