from threading import Thread
import socket
import constants
import time


class Timer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.serverAddress = None
        self.count = 0
        self.name = None
    
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        t = 0
        while True:
            time.sleep(1)
            t+=1
            if (t == self.count):
                msg = self.name + constants.TIMEOUT
                sock.sendto(msg.encode(), (self.serverAddress, constants.PORT))
                break
