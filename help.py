import client_server_controller
import constants

def menu():
    while True:
        choice = input('Bem vindo ao Quiz Game\n' +
        'Escolha uma opção de acordo com o número abaixo:\n\n' +
        '1 - Criar Partida\n' +
        '2 - Entrar em uma partida\n' + 
        '3 - Sair do Jogo\n' +
        '4 - Lista de Comandos\n' +
        '5 - Regras do jogo\n\n')

        if choice == '1':
            client_server_controller.createHostSession()
            break
        elif choice == '2':
            client_server_controller.createSession()
            break
        elif choice == '3':
            break
        elif choice == '4':
            commandsList()
        elif choice == '5':
            gameRules()
        else:
            print('Escolha um número válido\n\n')

def joinAnotherRoom(motive):
    while True:
        choice = input('Não foi possível entrar na sala, ' + motive + '\n' +
            'Escolha uma opção de acordo com o número abaixo:\n\n' +
            '1 - Tentar entrar em outra sala\n' +
            '2 - Voltar ao menu principal\n\n')

        if choice == '1':
            return True
        elif choice == '2' or choice == '\menu':
            return False
        else:
            print('Escolha uma opção válida: (\'1\' ou \'2\')\n\n')

def commandsList():
    while True:
        choice = input('\'/start\' - Para iniciar a partida\n' +
        '\'/quit\' - Para deixar a partida\n' +
        '\'/menu\' - Para retornar ao menu principal\n')

        if choice == '\menu':
            break
        else:
            print('Digite \'/menu\' para retornar ao menu principal')
        
def gameRules():
    print ('================================================================\n' +
'                          Regras do Jogo\n' +
    '================================================================\n\n' +
    '- Após o início da partida, não será permitido a entrada de novos participantes\n' +
    '- A rodada será encerrada quando um participante acertar a resposta ou atingir um tempo de 10 segundos\n' +
    '- Para resposta correta = ' + str(constants.TO_SCORE) + ' pontos; Para incorreta = -' + str(constants.TO_SCORE) + ' pontos; Sem resposta = -' + str(constants.TO_SCORE) + ' pontos\n' + 
    '- Cada partida terá ' + str(constants.MAX_ROUNDS) + ' rodadas\n' +
    '- A partida é composta de, no máximo, ' + str(constants.MAX_PLAYERS) + ' jogadores\n' +
    '- Não é permitido a entrada de novos participantes após o início da partida\n' + 
    '- Apenas o host pode dar início ao jogo\n' +
    '- Não é póssível acessar o menu enquanto a partida estiver em andamento\n\n')




