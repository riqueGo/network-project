from threading import Thread
import socket
import constants
import time


class Timer(Thread):
    def __init__(self, name, t, serverAddress):
        Thread.__init__(self)
        self.serverAddress = serverAddress
        self.timeout = t
        self.name = name
        self.on = True
        self.isRest = True
        self.count = 0

    
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while self.on:
            time.sleep(1)
            self.count+=1
            if self.count == self.timeout:
                msg = self.name + '#' + constants.TIMEOUT
                sock.sendto(msg.encode(), (self.serverAddress, constants.PORT))
                if self.name == constants.WAITING_ROOM:
                    break
                self.rest()
                self.count = 0
                self.isRest = True
    
    def rest(self):
        while self.isRest:
            continue