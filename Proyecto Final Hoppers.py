#########################################################################################################
# Maria Isabel Ortiz Naranjo                                                                            #
# 18176                                                                                                 #
# 03 de junio de 2021                                                                                   #
# Algoritmo minimax basado en: https://stackoverflow.com/questions/64644532/minimax-algorithm-in-python #
#########################################################################################################

from math import inf as infinity
from random import choice
import platform
import time
from os import system


# funcion mostrarMatriz
def mostrarMatriz(matriz):
    print ("   0  1  2  3  4  5  6  7  8  9")
    for x in range(10):
        print (x, matriz[x])

# funcion valida movimiento step
def validaStep(filai, coli, filaf, colf):
    bandera = False
    if (filaf-1) == filai or (filaf+1) == filai:
        if colf >= (coli-1) and colf <= (coli+1):
            bandera = True
    if (filaf == filai):
        if (coli-1) == colf or (coli+1) == colf:
            bandera = True
    return bandera

# funcion valida movimiento hope
def validaHope(filai, coli, filaf, colf):
    bandera = False
    if (filaf-2) == filai or (filaf+2) == filai or (filaf == filai):
        if colf == (coli-2) or colf == (coli+2):
            bandera = True
    return bandera

# funcion movimiento step
def step(filai, coli, filaf, colf, jugador):
    if validaStep(filai, coli, filaf, colf) == True:
        if matriz[filaf][colf] == 0:
            matriz[filaf][colf] = jugador
            matriz[filai][coli] = 0
        else:
            print ("La posicion final esta ocupada")
    else:
        print ("Movimiento invalido")

# funcion movimiento hope
def hope(filai, coli, filaf, colf, jugador):
    if validaHope(filai, coli, filaf, colf) == True:
        if matriz[filaf][colf]== 0:
            matriz[filaf][colf] = jugador
            matriz[filai][coli] = 0
        else:
            print ("La posicion final esta ocupada")
    else:
        print ("Movimiento invalido")

# Funcion cambiar jugador
def cambiarJugador(jugador):
    if jugador == 1:
        jugador = 2
    else:
        jugador = 1
    return jugador

# Funcion gana: cuando todas las fichas de un jugador estan en la posicion del otro jugador
def gana(jugador):
    cantidad1 = 0
    cantidad2 = 0
    #verifica si el jugador 1 llego a la esquina del jugador 2
    if jugador == 1: #computadora
        veces = 6
        fila = 9
        contfila = 0
        filas = 5
        while contfila < filas:
            veces = veces-1
            col = 9
            cont = 0
            while cont < veces:
                #print ("Col: ", col, "Cant1: ", cantidad1)
                if matriz[fila][col] == jugador: #jugador
                    cantidad1 = cantidad1 + 1
                cont = cont + 1
                col = col - 1
            fila = fila-1
            contfila = contfila+1
    if cantidad1 == 15: #gana el jugador 1
        return 1

    #verifica si el jugador 2 llego a la esquina del jugador 1
    if jugador == 2: #humano
        veces = 6
        fila = 0
        contfila = 0
        filas = 5
        while contfila < filas:
            veces = veces-1
            col = 0
            cont = 0
            while cont < veces:
                #print ("Col: ", col, "Cant2: ", cantidad2)
                if matriz[fila][col] == jugador: #jugador
                    cantidad2 = cantidad2 + 1
                cont = cont + 1
                col = col + 1
            fila = fila+1
            contfila = contfila+1
    if cantidad2 == 15: #gana el jugador 2
        return 2

    return 0 #no hay ganador

def evaluate():
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score
    """
    if gana(COMP) == 1:
        score = +1
    elif gana(HUMAN) == 2:
        score = -1
    else:
        score = 0
    return score

def wins(state, player): # gana(jugador)
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over():
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return gana(HUMAN) or gana(COMP)


def empty_cells():
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(matriz):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 100),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    #if depth == 0 or game_over() == 1 or game_over() == 2:
    #    score = evaluate()
    #    return [-1, -1, score]

    for cell in empty_cells():
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render( c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in matriz:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(board):
    """
    It calls the minimax function if the depth < 100,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells())
    if depth == 0 or game_over():
        return 0,0
    print (depth)
    print(f'Computer turn [{c_choice}]')
    #render(c_choice, h_choice)
    print ("voy")
    if depth == 100:
        x = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        y = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
        print (x, y)
    #set_move(x, y, COMP)
    return x, y
    time.sleep(0.01)


def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells())
    if depth == 0 or game_over():
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()

####################################
# Principal
####################################
# Inicializar variables
HUMAN = 2
COMP = 1
ganar = False
jugador = 1
h_choice = 2
c_choice = 1
# Definir matriz
matriz = [[1,1,1,1,1,0,0,0,0,0],
          [1,1,1,1,0,0,0,0,0,0],
          [1,1,1,0,0,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,2],
          [0,0,0,0,0,0,0,0,2,2],
          [0,0,0,0,0,0,0,2,2,2],
          [0,0,0,0,0,0,2,2,2,2],
          [0,0,0,0,0,2,2,2,2,2]]

mostrarMatriz(matriz)
filai=0
coli=0
filaf=0
colf=0
    
while (ganar == False):
    #Ingresar datos del movimiento: coordenada inicial y final
    print ("***Jugador***: ", jugador)
    if jugador == 2: #HUMANO
        filai = int (input("Fila inicial (0-9): "))
        coli = int (input("Columna inicial (0-9): "))
        filaf = int (input("Fila final (0-9): "))
        colf = int (input("Columna final (0-9): "))
    elif jugador == 1: #COMPUTADOR
        # el minimax me genere las coordenadas inicial y final
        filai, coli = ai_turn(matriz)
        print (filai, coli)
        filaf, colf = ai_turn(matriz)
        print (filaf, colf)
    opcion = input("¿step(s) o hope(h)?")
    #Step
    if opcion == "s":
        step(filai, coli, filaf, colf, jugador)
        mostrarMatriz(matriz)
        resultado = gana(jugador)
        if resultado == 1 or resultado == 2:
            ganar = True;
            print ("El jugador ", jugador, " ha ganado")
        else:
            jugador = cambiarJugador(jugador)
    #Hope
    if opcion == "h":
        hope(filai, coli, filaf, colf, jugador)
        mostrarMatriz(matriz)
        resultado = gana(jugador)
        if resultado == 1 or resultado == 2:
            ganar = True;
            print ("El jugador ", jugador, " ha ganado")
        else:
            jugador = cambiarJugador(jugador)

print ("fin del juego")