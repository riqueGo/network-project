import socket
import constants
from server import Server
from client import Client
from chat import Chat
from timer import Timer

def createHostSession():
    #Server Starts
    s = Server()
    s.start()

    #Instance of Timer Class
    timer = Timer(constants.WAITING_ROOM, 3, s.serverAddress)

    #Instance of Client class
    host = Client()
    host.serverAddress = s.serverAddress
    host.joinPlayer()

    #Starts client player
    host.start()

    #Starts Timer of waiting room
    timer.start()
    timer.join()
    host.join()

    turnOffServer(s)

def createSession():
    player = Client()
    player.joinTheGame()
    player.joinPlayer()
    player.start()


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

