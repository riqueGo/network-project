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
        elif choice == '2':
            client_server_controller.createSession()
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
        elif choice == '2':
            return False
        else:
            print('Escolha uma opção válida: (\'1\' ou \'2\')\n\n')

def commandsList():
    print('================================================================\n' +
'                          Comandos do Jogo\n' +
    '================================================================\n\n' +
    '\'/start\' - Para iniciar a partida (Apenas o host)\n' +
    '\'/quit\' - Para deixar a partida\n\n')

        
def gameRules():
    print ('================================================================\n' +
'                          Regras do Jogo\n' +
    '================================================================\n\n' +
    '- Após o início da partida, não será permitido a entrada de novos participantes\n' +
    '- A rodada será encerrada quando um participante acertar a resposta ou atingir um tempo de 10 segundos\n' +
    '- Para resposta correta = +' + str(constants.TO_SCORE) + ' pontos; Para incorreta = -' + str(constants.LOSE_SCORE) + ' pontos; Sem resposta = -' + str(constants.NO_SCORE) + ' pontos\n' + 
    '- Cada partida terá ' + str(constants.MAX_ROUNDS) + ' rodadas\n' +
    '- A partida é composta de, no máximo, ' + str(constants.MAX_PLAYERS) + ' jogadores\n' +
    '- Não é permitido a entrada de novos participantes após o início da partida\n' + 
    '- Apenas o host pode dar início ao jogo\n' +
    '- Não é póssível acessar o menu enquanto a partida estiver em andamento\n\n')




