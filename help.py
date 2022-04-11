import client_server_controller

def menu():
    while True:
        choice = input('Bem vindo ao Quiz Game\n' +
        'Escolha uma opção de acordo com o número abaixo:\n\n' +
        '1 - Criar Partida\n' +
        '2 - Entrar em uma partida\n' + 
        '3 - Sair do Jogo\n\n')

        if choice == '1':
            client_server_controller.createHostSession()
            break
        elif choice == '2':
            client_server_controller.createSession()
            break
        elif choice == '3':
            break
        else:
            print('Escolha uma opção válida: (\'1\' ou \'2\' ou \'3\')\n\n')

def joinAnotherRoom(motive):
    while True:
        choice = input('Não foi possível entrar na sala, ' + motive + '\n' +
            'Escolha uma opção de acordo com o número abaixo:\n\n' +
            '1 - Tentar entrar em outra sala\n' +
            '2 - Voltar ao menu principal\n\n')

        if choice == '1':
            return True
        elif choice == '2':
            return False
        else:
            print('Escolha uma opção válida: (\'1\' ou \'2\')\n\n')







