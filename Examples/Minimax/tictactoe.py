# Tic-Tac-Toe using the minimax algorithm
# DSM, 2017

# Change this line to control who goes first
human_moves_first = True

if human_moves_first:
    computer_symbol = 'O'
    human_symbol = 'X'
    turn_index = 0
else:
    computer_symbol = 'X'
    human_symbol = 'O'
    turn_index = 1


def wins(board, player):

    """Return True if the input player has three in a row"""

    # Row wins
    for i in range(3):    
        if (board[3 * i] == player and board[3 * i + 1] == player and 
            board[3 * i + 2] == player):
            return True

    # Column wins
    for i in range(3):    
        if (board[i] == player and board[i + 3] == player and 
            board[i + 6] == player):
            return True

    #Diagonal wins
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    # No win
    return False


def score(board):
    """Score a given board from the computer's perspective.

       Computer wins score 1 (best outcome for the computer)
       Human wins score -1 (worst outcome for the computer)
       Ties and incomplete games are 0
    """

    if wins(board, computer_symbol):
        return 1
    elif wins(board, human_symbol):
        return -1
    else:
        return 0


def minimax(board, depth, is_max_player):

    """Execute the minimax algorithm by exploring the subtree, identifying the
       move at each level that yields the best outcome for its player

       Returns: 
           the best score that the player can obtain in this subtree
           the move yielding that best score
    """

    # Base conditions: return a score
    current_score = score(board)
    if current_score != 0 or depth == 0:
        return current_score, None

    if is_max_player:
        best_value = -2 ** 40
        best_move = None

        for move in range(9):
            if board[move] != None:
                continue

            board[move] = computer_symbol

            value, response = minimax(board, depth - 1, False)

            if value > best_value:
                best_value = value
                best_move = move

            board[move] = None  # Reset the board

    if not is_max_player:
        best_value = 2 ** 40
        best_move = None

        for move in range(9):
            if board[move] != None:
                continue

            board[move] = human_symbol

            value, response = minimax(board, depth - 1, True)

            if value < best_value:
                best_value = value
                best_move = move

            board[move] = None

    return best_value, best_move


def display(board):
    print('')

    for i in range(9):
        if board[i] is None:
            print('.  ', end='')
        else:
            print(board[i], ' ', end='')

        if i == 2 or i == 5 or i == 8:
            print('')

    print('')


def get_move(board):
    looping = True;

    while looping:
        looping = False

        print('Enter a board position, 0-8: ', end='')
        move = int(input())

        if (board[move] != None) or move < 0 or move > 9:
            print('Choose a different position.')
            looping = True

    return move


def play():
    board = {0: None, 1: None, 2: None,
             3: None, 4: None, 5: None,
             6: None, 7: None, 8: None}

    print('0  1  2\n3  4  5\n6  7  8')

    turn = 0

    while turn < 9:

        # Human turn
        if turn % 2 == turn_index:
            move = get_move(board)
            board[move] = human_symbol

        # Computer turn
        else:
            best_value, best_move = minimax(board, 9 - turn, True)
            board[best_move] = computer_symbol

        display(board)

        # Check for wins
        if wins(board, human_symbol):
            print('Man triumphs over machine!')
            turn = 9
        elif wins(board, computer_symbol):
            print('A dark day for humanity...')
            turn = 9

        turn += 1

    if turn == 9:  
        print('The only winning move is not to play.')

if __name__ == '__main__':
    play()
