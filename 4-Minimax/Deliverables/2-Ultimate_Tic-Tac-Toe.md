# Ultimate Tic-Tac-Toe

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Super_tic-tac-toe_rules_example.png/500px-Super_tic-tac-toe_rules_example.png" width="300px" />

*Via Wikipedia*.

## Overview

In 2009, I was teaching computer science for a summer high school program. In the downtime of our classes, the students in the class kept playing this tic-tac-toe variant I had never seen before: **Ultimate Tic-Tac-Toe**.

UTTT is played on a 3x3 grid, where each position is a 3x3 tic-tac-toe board. Winning one of the sub-games gives your piece control of its square on the large board. The object is to win the tic-tac-toe game on the large board.

## Rules

1. X goes first and may move to any of the 81 individual board locations.

2. The position chosen by X determines the board that O must use for its next move. If X chose the upper-left position of its smaller board then O's next move must go on the upper-left game of the large board.

3. This process repeats: the position chosen by O on the small board determines which game of the large board X must move onto next.

4. When either player wins a small board, it's marked with their symbol and no further moves there are allowed. If a player would be sent to a cleared board by the normal rules of play, they're allowed to choose any active board for their next move.

5. The game continues until one player wins the tic-tac-toe game on the large board, or no winner is possible, in which case the game is a draw.




## Strategy

