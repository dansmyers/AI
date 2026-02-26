# Subtraction Game

## Overview

The subtraction game is a simple mathematical strategy game. Beginning with a pile of 21 stones, players alternate removing stones until none are left. On her turn, a player may take 1, 2, or 3 stones. The player who takes the last stone is the winner in this version. The game was played on an episode of *Survivor: Thailand* where it was called *Thai 21*.

The implementation below demonstrates the basic minimax algorithm with a depth limit for playing the subtraction game. Try playing the game against the computer opponent and see how well you do. Can you win? How does the computer's performance change if you adjust the depth limit?

## Code

```
"""
The Subtraction Game

Beginning with a pile of 21 stones, players alternate removing stones until
none are left. On her turn, a player may take 1, 2, or 3 stones. The player
who takes the last stone is the winner in this version.
"""

# Change this line to control who goes first
human_moves_first = True

def minimax(stones, depth, is_max_player):

    """Minimax algorithm for the subtraction game

    Args:
        stones: remaining stones
        depth: remaining levels of search
        is_max_player: True if the current call corresponds to the maximizing player
                       False if the current call is for the minimizing player

    Returns: 
        the best score that the player can obtain in this subtree
        the move yielding that best score
    """

    # If there are no stones left, this player has lost (the previous player reduced
    # stones to 0 on their most recent turn)
    #
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

    # The maximizing player wants to obtain the highest possible score
    #
    # Start with a very small score and use the recursive minimax approach
    # to discover if there's any possible move that yields a better value
    if is_max_player:
        best_value = -10
        best_remove = None  # Best number of stones to take

        for remove in [1, 2, 3]:

            value, response = minimax(stones - remove, depth - 1, False)

            if value > best_value:
                best_value = value
                best_remove = remove

    # The min player wants to obtain the lowest possible score
    #
    # This code is symmetric to the max player, but starts with a large score
    # and searches for the move yielding the smallest outcome              
    if not is_max_player:

        best_value = 10
        best_remove = None  # Best number of stones to take

        for remove in [1, 2, 3]:

            value, response = minimax(stones - remove, depth - 1, True)

            if value < best_value:
                best_value = value
                best_remove = remove


    return best_value, best_remove


def get_move(stones):
    looping = True;

    while looping:
        looping = False

        remove = int(input('Remove 1, 2, or 3 stones: '))

        if remove < 1 or remove > 3 or remove > stones:
            print('That is not a valid move.')
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

        print('\n' + stones)

        # Human move
        if turn % 2 == turn_index:
            remove = get_move(stones)
            stones -= remove

        # Computer move
        else:
            value, remove = minimax(stones, 5, True)
            print("I'll take %d." % remove)
            stones -= remove

        # The player who took the last stone is the winner
        if stones == 0:
            if turn % 2 == turn_index:
                print('\nMy...failure...DOES NOT COMPUTE.')
            else:
                print('\nSoft flesh will never defeat cold steel.')

            playing = False    

        turn += 1


if __name__ == '__main__':
    play()
```
