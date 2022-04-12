#Game Settings
PORT = 12000 #sudo netstat -ap | grep :12000
MAX_ROUNDS = 5
MAX_PLAYERS = 5
TO_SCORE = 25
LOSE_SCORE = 5
NO_SCORE = 1
HOST_ADDRESS = ['0.0.0.0', '127.0.1.1', '127.0.0.1']


# From Server to Client Messages
DISCONNECTED_SERVER = 'SERVIDOR DESCONECTADO'
START_ROUND = 'START ROUND'
ANSWER = 'ANSWER'
WRONG_ANSWER = 'Você Errou! Perdeu ' + str(LOSE_SCORE) + ' Pontos'
CORRECT_ANSWER = 'Acertou! ganhou ' + str(TO_SCORE) + ' Pontos'
LOTATION_MESSAGE = 'partida lotada'
GAME_RUNNING = 'jogo em andamento'
GAME_ENDED = 'Acabou o Jogo'
PRINT_MESSAGE = 'PRINT MESSAGE'


# From Client to Server Messages
ADD_PLAYER = 'ADD PLAYER'
REMOVE_PLAYER = 'saiu do Jogo'
QUIT = '/QUIT'
CHAT = 'CHAT'
START_COMMAND = '/START'
GAME_START = 'O jogo vai começar'
INVALID_ADDRESS = 'Endereço Inválido'


# Manipulation Messages
ALL_PLAYER_MESSAGE = 'ALL PLAYER MESSAGE'
SINGLE_PLAYER_MESSAGE = 'SINGLE PLAYER MESSAGE'
TIMEOUT = 'TIMEOUT'
