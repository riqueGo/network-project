import clinet_server_controller

def menu():
    while True:
        choice = input('Bem vindo ao Quiz Game\n' +
        'Escolha uma opção de acordo com o número abaixo:\n\n' +
        '1 - Criar Partida\n' +
        '2 - Entrar em uma partida\n\n')

        if choice == '1':
            clinet_server_controller.createHostSession()
            break
        elif choice == '2':
            clinet_server_controller.createSession()
            break
        else:
            print('Escolha uma opção válida: (\'1\' ou \'2\')\n\n')







