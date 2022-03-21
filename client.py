import socket
import constants

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_adress = self.get_local_ip()

    def sendMessage(self):
        while True:
            msg_send = input('Digite uma mensagem: ')
            print(self.client_adress)
            self.client.sendto(msg_send.encode(),(self.client_adress,constants.PORT))
            msg_bytes, ip_serv = self.client.recvfrom(2048)
            print(msg_bytes.decode())
            
            if msg_bytes.decode() == constants.LOTATION_MESSAGE:
                break
    
    def get_local_ip(self):
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