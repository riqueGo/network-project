from socket import socket, AF_INET, SOCK_STREAM
from _thread import *

host = 'localhost'
porta = 80
modelo = "modelo.html"

def servidor(socket_client):
    while True:
        data = socket_client.recv(2048)
        if not data:
            break
        data_decodif = data.decode()
        metodo = data_decodif.split(' ')[0]
        requisicao = data_decodif.split(' ')[1]
        print('Requisição do cliente:', requisicao, metodo)
        meu_arquivo = requisicao.lstrip('/')
        if meu_arquivo == '':
            meu_arquivo = 'modelo.html'
        try:
            arquivo = open(meu_arquivo,'rb')
            arquivo_lido = arquivo.read()
            arquivo.close()
            if meu_arquivo.endswith('.html'):
                mimetype = 'text/html'
            elif meu_arquivo.endswith('.htm'): #nao testei
                mimetype = 'text/htm'
            elif meu_arquivo.endswith('.txt'):
                mimetype = 'text/txt'
            elif meu_arquivo.endswith('.css'):
                mimetype = 'text/css'
            elif meu_arquivo.endswith('.js'): #nao está dando muito bom
                mimetype = 'aplication/js'
            elif meu_arquivo.endswith('.pdf'):
                mimetype = 'application/pdf'
            elif meu_arquivo.endswith('.docx'):
                mimetype = 'application/docx'
            elif meu_arquivo.endswith('.png'):
                mimetype = 'image/png'
            elif meu_arquivo.endswith('.gif'):
                mimetype = 'image/gif'
            else:
                mimetype = 'image/jpg'
            header = 'HTTP/1.1 200 OK\n'
            header += 'Content-Type: ' + str(mimetype) + '\n\n'
        except:
            #erros 400 Bad Request, 404 ou 505 HTTP Version Not Supported
            header = 'HTTP/1.1 404 Not Found\n\n'
            arquivo_lido = '<html><body><center><h3>Error 404: File not found</h3><p>Documento requisitado nao foi localizado no servidor</p></center></body></html>'
            arquivo_lido = arquivo_lido.encode('utf-8')
        resposta_final = header.encode('utf-8')
        resposta_final += arquivo_lido
        socket_client.send(resposta_final)
        break

def main():
    socket_server = socket(AF_INET, SOCK_STREAM)
    socket_server.bind((host, porta))
    socket_server.listen(3)
    while True:
        socket_client, endereco_cliente = socket_server.accept()
        start_new_thread(servidor,(socket_client,))
        print(f'Conectado com: {endereco_cliente[0]}:{endereco_cliente[1]}')

if __name__ == "__main__":
    main()








