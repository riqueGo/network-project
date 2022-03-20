import socket
import constants


# cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     msg_envio = input('Digite a mensagem: ')
#     cliente.sendto(msg_envio.encode(),('192.168.1.26',constants.PORT))
#     msg_bytes, ip_serv = cliente.recvfrom(2048)
#     print(msg_bytes.decode())
#     if msg_bytes.decode() == constants.LOTATION_MESSAGE:
#         break

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def sendMessage(self):
        while True:
            msg_envio = input('Digite a mensagem: ')
            self.client.sendto(msg_envio.encode(),('192.168.1.26',constants.PORT))
            msg_bytes, ip_serv = self.client.recvfrom(2048)
            print('Client: ' + msg_bytes.decode())
            
            if msg_bytes.decode() == constants.LOTATION_MESSAGE:
                break