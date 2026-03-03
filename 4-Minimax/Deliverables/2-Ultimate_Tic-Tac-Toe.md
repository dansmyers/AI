# Ultimate Tic-Tac-Toe

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Super_tic-tac-toe_rules_example.png/500px-Super_tic-tac-toe_rules_example.png" width="300px" />

*Via Wikipedia*.

## Overview

In 2009, I was teaching computer science for a summer high school program. In the downtime of our classes, the students in the class kept playing this tic-tac-toe variant I had never seen before: **Ultimate Tic-Tac-Toe**.

UTTT is played on a 3x3 tic-tac-toe board, where each position is itself a smaller 3x3 tic-tac-toe board. Players make moves to the small boards. Winning one of the small games gives your piece control of its position on the large board. The object is to win the tic-tac-toe game on the large board.

## Rules

1. X goes first and may move to any of the 81 individual board locations.

2. The position chosen by X determines the board that O must use for its next move. If X chose the upper-left position of its smaller board then O's next move must go on the upper-left game of the large board.

3. This process repeats: the position chosen by O on the small board determines which game of the large board X must move onto next.

4. When either player wins a small board, it's marked with their symbol and no further moves there are allowed. If a player would be sent to a cleared board by the normal rules of play, they're allowed to choose any active board for their next move.

5. The game continues until one player wins the tic-tac-toe game on the large board, or no winner is possible, in which case the game is a draw.

The movement rules make the game strategically more complex that traditional tic-tac-toe. The best moves combine making tactical progress on the small boards while managing the strategic situation on the large boards. It may be desirable to make a locally poor move to force your opponent to play on a particular small board.

You can see how this game would be hard for the standard minimax algorithm: the branching factor is high and it's hard to evaluate the quality of positions. It is, however, a good fit for Monte Carlo tree search, because the game lends itself to rollouts by making random moves.

## Project

Implement a web-based version of ultimate tic-tac-toe using Monte Carlo tree search for the game AI.

- Use the UCB1 tree descent policy
- On the rollout stage, make random moves at each step until you reach a concluding state
- Award a score of +1 for a win to the current player, -1 for a loss, and 0 for a draw
- Play around with different settings for the maximum number of iterations for the search
- At the end of the search, choose the top-level move with the best expected outcome
