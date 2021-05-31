import os

board = {
    'slots': [7,8,9,4,5,6,1,2,3],
    'winner_moves': [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]],
}

players = {
    'player_1': {
        'symbol': '',
        'moves': [],
    },
    'player_2': {
        'symbol': '',
        'moves': [],
    },
    'current_turn': 'player_1',
    'winner': '',
}

game_is_on = True

# Function to display a 3 x 3 board from a list of 9 items
def display_board(board):
    for x in range(0,9,3):
        print(f"{' ' if board['slots'][x] not in ['O', 'X'] else board['slots'][x]}|\
{' ' if board['slots'][x+1] not in ['O', 'X'] else board['slots'][x+1]}|\
{' ' if board['slots'][x+2] not in ['O', 'X'] else board['slots'][x+2]}")

    print('\n')


def assign_symbol_to_user(players):
    # Checking player 1 is enough, since we will automatically assign the other symbol to player 2
    while len(players['player_1']['symbol']) == 0:
        user_input = input('Please, choose symbol for player 1 (X or O) -> ').upper()
        if user_input in ['X', 'O']:
            players['player_1']['symbol'] = user_input
            players['player_2']['symbol'] = 'O' if user_input == 'X' else 'X'
        else:
            os.system('cls')
            assign_symbol_to_user(players)

    return players


def check_move(board, move):
    # Since our board is built with integers, any non-integer (0-9) slot is already taken
    free_slots = [str(slot) for slot in board['slots'] if slot in range(0,10)]
    
    return move in free_slots


def check_digit(move):
    valid_digits = [str(num) for num in range(0, 10)]

    return move in valid_digits


def assign_move_player(players, player, move):
    players[player]['moves'].append(int(move))


def player_move(board,player,players):
    move = ''

    while not check_move(board, move) or not check_digit(move):
        move = input('Choose a slot to assign the mark -> ')

    slot_index = board['slots'].index(int(move))
    board['slots'][slot_index] = players[player]['symbol']

    assign_move_player(players, player, move)

    return board


def check_winner(players,board):
    for move in board['winner_moves']:
        count_p1 = 0
        count_p2 = 0
        for num in move:
            if num in players['player_1']['moves']:
                count_p1 += 1
            elif num in players['player_2']['moves']:
                count_p2 += 1
            else:
                pass

        if count_p1 == 3 or count_p2 == 3:
            return True

    return False


def check_tie(board):
    board_status = list(set([str(slot) for slot in board['slots']]))
    board_status.sort()

    return ['O', 'X'] == board_status


def end_game(board):
    os.system('cls')
    display_board(board)

# Final game logic
def game(players, board, game_is_on):
    # Game intro
    print('''
    TIC TAC TOE

    - The board is organized as follows:
        7|8|9
        4|5|6
        1|2|3

    - Players will take turns and pick a slot to assign their mark

    ENJOY!
    ''')
    players = assign_symbol_to_user(players)

    while game_is_on:
        os.system('cls')
        display_board(board)
        print(f"{players['current_turn']} turn\n")
        board = player_move(board, players['current_turn'], players)

        if check_winner(players, board):
            end_game(board)
            print(f"{players['current_turn']} wins!")
            game_is_on = False
        elif check_tie(board):
            end_game(board)
            print('It is a tie!')
            game_is_on = False
        else:
            players['current_turn'] = 'player_2' if players['current_turn'] == 'player_1' else 'player_1'


game(players, board, game_is_on)