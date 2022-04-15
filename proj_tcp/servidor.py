from socket import socket, AF_INET, SOCK_STREAM

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 9000))

while True:
    server_socket.listen()
    client_socket, address_client = server_socket.accept()

    print("Cliente conectado!")

    data = client_socket.recv(2048)

    dados = data.decode()

    print(f'{dados}')

    client_socket.close()