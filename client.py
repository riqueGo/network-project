import socket
import constants


cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg_envio = input('Digite a mensagem: ')
    cliente.sendto(msg_envio.encode(),('192.168.15.137',12001))
    msg_bytes, ip_serv = cliente.recvfrom(2048)
    print(msg_bytes.decode())
    if msg_bytes.decode() == constants.LOTATION_MESSAGE:
        break