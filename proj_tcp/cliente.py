from socket import socket, AF_INET, SOCK_STREAM

TCPSocket = socket(AF_INET, SOCK_STREAM)
print("Eu sou o cliente!")

address = 'localhost', 9000
TCPSocket.connect(address)

mensagem = input("\nDigite uma mensagem p/ enviar: ")
mensagem_codificada = mensagem.encode()
TCPSocket.send(mensagem_codificada)
input("Conexão finalizada!")
