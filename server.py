import socket
import player
import constants
bind_ip = ''
bind_port = 12001
max_player = 5

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('',bind_port))
player_connected = dict()


while True:
    msg_bytes, ip_cliente = servidor.recvfrom(2048)
    if len(player_connected.keys()) < max_player and ip_cliente not in player_connected.keys():
        player_connected[ip_cliente[0]] = player.Player(len(player_connected))
        msg_resp = 'Player ' + str(len(player_connected)) + ' connected'
        servidor.sendto(msg_resp.encode(), ip_cliente)
        print(msg_resp)
        print(player_connected)
    elif len(player_connected.keys()) >= max_player and ip_cliente not in player_connected.keys():
        msg_resp = constants.LOTATION_MESSAGE
        servidor.sendto(msg_resp.encode(), ip_cliente)
        continue
    else:
        msg_resp = 'você ja esta conectado'
        servidor.sendto(msg_resp.encode(), ip_cliente)
