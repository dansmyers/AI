# The Subtraction Game with Alpha-Beta pruning
# DSM, 2017

# Beginning with a pile of 21 stones, players alternate removing stones until
# none are left. On her turn, a player may take 1, 2, or 3 stones. The player
# who takes the last stone is the winner.

# Change this line to control who goes first
human_moves_first = True

def minimax(stones, depth, alpha, beta, is_max_player):

    """Execute the minimax algorithm by exploring the subtree, identifying the
       move at each level that yields the best outcome for its player

       Returns: 
           the best score that the player can obtain in this subtree
           the move yielding that best score
    """

    # If there's no stones left, this player has lost
    # If the max player has lost, return -1 (worst outcome for max)
    # If the min player has lost, return 1 (best outcome for max)
    if stones == 0:
        if is_max_player:
            return -1, 0
        else:
            return 1, 0

    # If the depth limit has been reached, return 0
    if depth == 0:
        return 0, None

    if is_max_player:
        best_value = -10
        best_remove = None

        for remove in [1, 2, 3]:
            value, response = minimax(stones - remove, depth - 1, alpha, beta, False)


            if value > best_value:
                best_value = value
                best_remove = remove

            if value >= beta:
                break

            alpha = max(alpha, value)

  
    if not is_max_player:
        best_value = 10
        best_remove = None

        for remove in [1, 2, 3]:
            value, response = minimax(stones - remove, depth - 1, alpha, beta, True)

            if value < best_value:
                best_value = value
                best_remove = remove

            if value <= alpha:
                break

            beta = min(beta, value)


    return best_value, best_remove


def get_move(stones):
    looping = True;

    while looping:
        looping = False

        print('Remove 1, 2, or 3 stones: ', end='')
        remove = int(input())

        if remove < 1 or remove > 3:
            print('You can only take 1, 2, or 3.')
            looping = True

    return remove


def play():

    stones = 21

    playing = True
    turn = 0

    if human_moves_first:
        turn_index = 0
    else:
        turn_index = 1

    while playing:

        print('')
        print(stones)

        # Human move
        if turn % 2 == turn_index:
            remove = get_move(stones)
            stones -= remove

        # Computer move
        else:
            value, remove = minimax(stones, 20, -10, 10, True)
            print ("I'll take %d." % remove)
            stones -= remove

        # The player who took the last stone is the winner
        if stones == 0:
            if turn % 2 == turn_index:
                print('\nMy...failure...DOES NOT COMPUTE.')
            else:
                print('\nWeep, soft human.')

            playing = False    

        turn += 1


if __name__ == '__main__':
    play()
