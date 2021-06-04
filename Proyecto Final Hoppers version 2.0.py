from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
Maria Isabel Ortiz Naranjo
Carne: 18176
An implementation of Minimax AI Algorithm in Hoppers,
using Python
"""

HUMAN = -1
COMP = +1
board = [
     [1,1,1,1,1,0,0,0,0,0],
     [1,1,1,1,0,0,0,0,0,0],
     [1,1,1,0,0,0,0,0,0,0],
     [1,1,0,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,2,2],
     [0,0,0,0,0,0,0,2,2,2],
     [0,0,0,0,0,0,2,2,2,2],
     [0,0,0,0,0,2,2,2,2,2]
]



def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player): # gana(jugador)
    """
    This function tests if a specific player wins. Possibilities:
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    #gana el jugador computadora (+1) cuando todos los unos se pasan abajo
    win_state1 = [[state[5][9]],
                  [state[6][9]],
                  [state[7][9]],
                  [state[8][9]],
                  [state[9][9]],
                  [state[6][8]],
                  [state[7][8]],
                  [state[8][8]],
                  [state[9][8]],
                  [state[7][7]],
                  [state[8][7]],
                  [state[9][7]],
                  [state[8][6]],
                  [state[9][6]],
                  [state[9][5]],
                  ]
 
    #gana el jugador humano (-1) cuando todos los dos se pasan arriba
    
    win_state2 = [[state[0][0]],
                  [state[0][1]],
                  [state[0][2]],
                  [state[0][3]],
                  [state[0][4]],
                  [state[1][0]],
                  [state[1][1]],
                  [state[1][2]],
                  [state[1][3]],
                  [state[2][0]],
                  [state[2][1]],
                  [state[2][2]],
                  [state[3][0]],
                  [state[3][1]],
                  [state[4][0]],
                  ]
    
    if player == 1:
        if [player, player, player, player, player, player, player, player, player, player, player, player, player, player] in win_state1:
            return True
        else:
            return False
    
    if player == -1:
        if [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] in win_state2:
            return True
        else:
            return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []
    for x, row in enumerate(state):
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


def set_move(x, y, player, xi, yi):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        board[xi][yi] = 0
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
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


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {
        2: h_choice,
        1: c_choice,
        0: ' '
    }
    str_line = '--------------------------------------------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            #print(cell)
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice, xi, yi):
    """
    It calls the minimax function if the depth < 70,
    else it choices a random coordinate.
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 70:
        x = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        y = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
    
    set_move(x, y, 1, xi, yi)
    time.sleep(1)


def human_turn(c_choice, h_choice,xi,yi):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice 1
    :param h_choice: human's choice 2
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
         0: [0, 0], 1: [0, 1], 2: [0, 2], 3: [0, 3], 4: [0, 4], 5: [0, 5], 6: [0, 6], 7: [0, 7], 8: [0, 8], 9: [0, 9],
        10: [1, 0], 11: [1, 1], 12: [1, 2], 13: [1, 3], 14: [1, 4], 15: [1, 5], 16: [1, 6], 17: [1, 7], 18: [1, 8], 19: [1, 9],
        20: [2, 0], 21: [2, 1], 22: [2, 2], 23: [2, 3], 24: [2, 4], 25: [2, 5], 26: [2, 6], 27: [2, 7], 28: [2, 8], 29: [2, 9],
        30: [3, 0], 31: [3, 1], 32: [3, 2], 33: [3, 3], 34: [3, 4], 35: [3, 5], 36: [3, 6], 37: [3, 7], 38: [3, 8], 39: [3, 9],
        40: [4, 0], 41: [4, 1], 42: [4, 2], 43: [4, 3], 44: [4, 4], 45: [4, 5], 46: [4, 6], 47: [4, 7], 48: [4, 8], 49: [4, 9],
        50: [5, 0], 51: [5, 1], 52: [5, 2], 53: [5, 3], 54: [5, 4], 55: [5, 5], 56: [5, 6], 57: [5, 7], 58: [5, 8], 59: [5, 9],
        60: [6, 0], 61: [6, 1], 62: [6, 2], 63: [6, 3], 64: [6, 4], 65: [6, 5], 66: [6, 6], 67: [6, 7], 68: [6, 8], 69: [6, 9],
        70: [7, 0], 71: [7, 1], 72: [7, 2], 73: [7, 3], 74: [7, 4], 75: [7, 5], 76: [7, 6], 77: [7, 7], 78: [7, 8], 79: [7, 9],
        80: [8, 0], 81: [8, 1], 82: [8, 2], 83: [8, 3], 84: [8, 4], 85: [8, 5], 86: [8, 6], 87: [8, 7], 88: [8, 8], 89: [8, 9],
        90: [9, 0], 91: [9, 1], 92: [9, 2], 93: [9, 3], 94: [9, 4], 95: [9, 5], 96: [9, 6], 97: [9, 7], 98: [9, 8], 99: [9, 9],
        
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)
    while move < 0 or move > 99:
        try:
            move = int(input('Final position HUMAN (0..99): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], 2, xi, yi)
            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = '2'  # 
    c_choice = '1'  # 
    first = ''  # if human is the first

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            print(" $$\   $$\  $$$$$$\  $$$$$$$\  $$$$$$$\  $$$$$$$$\ $$$$$$$\   $$$$$$\ ")   
            print(" $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ $$  __$$\ ")
            print(" $$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ /  \__|")
            print(" $$$$$$$$ |$$ |  $$ |$$$$$$$  |$$$$$$$  |$$$$$\    $$$$$$$  |\$$$$$$\  ")
            print(" $$  __$$ |$$ |  $$ |$$  ____/ $$  ____/ $$  __|   $$  __$$<  \____$$\ ")
            print(" $$ |  $$ |$$ |  $$ |$$ |      $$ |      $$ |      $$ |  $$ |$$\   $$ |")
            print(" $$ |  $$ | $$$$$$  |$$ |      $$ |      $$$$$$$$\ $$ |  $$ |\$$$$$$  |")
            print(" \__|  \__| \______/ \__|      \__|      \________|\__|  \__| \______/ ")                                         
                                                                    
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
                
        if first == 'N':
            print("Step")
            xi = int (input("Initial row COMP(0-9): "))
            yi = int (input("Initial column COMP(0-9): "))
            ai_turn(c_choice, h_choice, xi, yi)
            first = ''
        render(board, c_choice, h_choice)
        print("Hope")
        xi = int (input("Initial row HUMAN(0-9): "))
        yi = int (input("Initial column HUMAN(0-9): "))
        human_turn(c_choice, h_choice,xi,yi)
        render(board, c_choice, h_choice)
        xi = int (input("Initial row COMP(0-9): "))
        yi = int (input("Initial column COMP(0-9): "))
        ai_turn(c_choice, h_choice, xi, yi)

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


if __name__ == '__main__':
    main()
