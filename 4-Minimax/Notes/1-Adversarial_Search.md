# Adversarial Search

## Overview

Our previous units considered variations on tree search, where the goal was to find a plan that moved from a starting state to a goal state, sometimes under the requirement to find the plan of minimum cost.

We're now going to consider a variation: what if there is an *opponent* who seeks to thwart your moves? Consider a typical turn-based strategic game like tic-tac-toe or chess. You and your opponent alternate moves. On your turn, you always seek the best move; that is, the one that maximizes your chance of winning the game. Your opponent is doing the same from their own perspective - their best move is *your worst move*.

The main algorithm for this unit is the **minimax algorithm** which finds the best move at each step of an adversarial game under the assumption that both players are playing rationally and optimally. That is, I'm trying my best to win on my turn, and my opponent is trying the best to win on his turn.

This set-up leads to a tree of potential moves, alternating turns:

- For the current situation, I have a set of potential moves
- Then my opponent has a set of potential countermoves to each one of my moves
- And I have a set of counter-counter moves in response to his moves
- And so forth, alternating his responses and my responses, until we construct the entire game tree of potential future states

The minimax algorithm tells you how to choose the best top-level move that maximizes your long-term outcome over the entire game, under the assumption that your opponent is making rational responses to maximize *their own* long-term outcome.

## Tic-Tac-Toe

Consider the following tic-tac-toe board, where it's **O's turn** to play next.
```
 O | X | O
-----------
   | X | X
-----------
   | O | X
```
There are two possible moves O can make: the center-left and lower-left. What happens in each case?

- If O takes the center-left square, X takes the lower-left and the outcome is a tie
- If O takes the lower-left, then X wins by completing the middle row

Consider another board for **X's turn**:
```
 X |   | 
-----------
 O |   | 
-----------
 X |   | O
```
Suppose that X takes the top-middle square. We can consider the entire sequence of game moves under that assumption and build the entire tree of potential future game states.

<img src="./Images/tictactoe_game_tree.png" width="600px" />

Observe that the best outcome X can obtain through this choice is a *tie*. There is no path in the game tree that leads to a win if X takes the top-middle square.

### Practice

Repeat the previous example, but choose the top-right for X's move. Build out the game tree and show that X now has a guaranteed win through this move.

## Intuition

The tic-tac-toe example is simple, but illustrates some important concepts for adversarial two-player games:

- First, we should assume that the opponent is rational and will always choose strategically optimal moves. We shouldn't expect to win because the opponent blundered and make a bad move.

- Second, playing out the game tree for each possible move choice can reveal if a move is good or bad. In the example above, the game trees show that the top-right leads to a guaranteed win, so we should choose that move.


