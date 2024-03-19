# Connect Four

## Due April 2

## You can work with a partner to complete this project

<img src="https://upload.wikimedia.org/wikipedia/en/7/79/Connect_4_Board_and_Box.jpg" width="400px" />

<br/>

## Overview

*Connect Four* is a popular game marketed by Milton-Bradley. In the former days it was knows as *Captain's Mistress*: The South Seas explorer Captain Cook was
allegedly quite fond of it.

The game is played on a 6 row by 7 column grid suspended vertically. On his turn, a player drops one of his pieces into any column that is not already full. The piece drops down the column until it reaches the bottom or lands on top of
another piece. Once placed, pieces are never moved. The  rst player to place
four pieces in a row|horizontally, vertically, or diagonally|is the winner. If
the board  lls without either player making a row, the game is declared a draw.

Create an implementation of Connect Four that allows a human to play against
a computer opponent. Your game should use the minimax algorithm with alpha-
beta pruning to determine the strategy for the AI player. Use a coin 
ip at the
start of the game to determine who gets to move  rst. You can use text to
visualize the board, but make it clear how the user should input each move, for
example as numbers 0-6 or 1-7, or as letters A-G.
The moves at each step are simple, but the game has a high branching factor.
Therefore, you might need to carefully adjust the depth limit of the AI search
to keep the game playable.
