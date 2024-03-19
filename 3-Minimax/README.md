# Connect Four

## Due April 2

## You can work with a partner to complete this project

<img src="https://upload.wikimedia.org/wikipedia/en/7/79/Connect_4_Board_and_Box.jpg" width="400px" />

<br/>

## Overview

*Connect Four* is a popular game marketed by Milton-Bradley. In the former days it was knows as *Captain's Mistress*: The South Seas explorer Captain Cook was
allegedly quite fond of it.

The game is played on a 6 row by 7 column grid suspended vertically. On each turn, a player drops one piece into any column that is not already full. The piece drops down the column until it reaches the bottom or lands on top of another piece. Once placed, pieces are never moved. The  first player to place four pieces in a row|horizontally, vertically, or diagonally is the winner. If the board fills without either player making a row of four, the game is declared a draw.

Create an implementation of Connect Four that allows a human to play against a computer opponent. Your game should use the minimax algorithm with alpha-beta pruning to determine the strategy for the AI player. Use a coin  flip at the start of the game to determine who gets to move  first. You can use text to visualize the board, but make it clear how the user should input each move, for example as numbers 0-6 or 1-7, or as letters A-G. 

The moves at each step are simple, but the game has a high branching factor. Therefore, you might need to carefully adjust the depth limit of the AI search to keep the game playable.

## Deliverables

<img src="https://www.samsonhistorical.com/cdn/shop/products/Captains-Mistress-table-top-game_600x.jpg?v=1665146950" width="400px" />

*Captain's Mistress by [Samson Historical](https://www.samsonhistorical.com/products/captains-mistress)*

<br/>

Write one script called `connect_four.py` that contains all of the code for the game.

- You must use the minimax algorithm with alpha-beta pruning. Look at the example programs in the `Examples` directory.

- Use a 7-column by 6-row board.

- You'll need to check for the winning condition each time you add a piece. Remember that the winning piece can complete any group of four horizontally, vertically, or diagonally.

- Programmed properly, the game should be very difficult to beat. If you can win easily, you need to either increase the depth of your game tree, or recheck your solution.

- Submit your program to the assignment I'll create on Canvas. If you work with a partner, include their name at the top of your code.


## Tips

Develop incrementally!

- Start by writing a simple version of the game for one player that allows you to add pieces, prints the board, and identifies four in a row
- Then extend to two human players
- Then replace one human player with the basic minimax algorithm
- Then add alpha-beta pruning

The tic-tac-toe example is very relevant.
