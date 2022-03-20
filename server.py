import socket
import player
import constants
from threading import Thread

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.ip_addess = ''
        self.port = constants.PORT
        self.max_player = 5
        self.player_connected = dict()
        self.server = self.createServer()

    def createServer(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((self.ip_addess, self.port))
        print('Server: Server started')
        return server
    
    def run(self):
        while True:
            msg_bytes, client_adress = self.server.recvfrom(2048)
            if len(self.player_connected.keys()) < self.max_player and client_adress[0] not in self.player_connected.keys():
                self.player_connected[client_adress[0]] = player.Player(len(self.player_connected))
                msg_resp = 'Server: Player ' + str(len(self.player_connected)) + ' connected'
                self.server.sendto(msg_resp.encode(), client_adress)
            elif len(self.player_connected.keys()) >= self.max_player and client_adress[0] not in self.player_connected.keys():
                msg_resp = 'Server: ' + constants.LOTATION_MESSAGE
                self.server.sendto(msg_resp.encode(), client_adress)
                continue
            else:
                msg_resp = 'Server: você ja esta conectado'
                self.server.sendto(msg_resp.encode(), client_adress)