# Minimax and Game AI

<img src="https://www.kasparov.com/wp-content/uploads/2014/06/deep-blue-kasparov.jpg" width="400px" />

*The famous match between world champion Garry Kasparov and IBM's Deep Blue chess computer in May 1997. Kasparov was the world's dominant player and the then-highest rated player in chess history. Deep Blue's victory was the first time a chess program defeated a world champion under standard tournament conditions. Via [kasparov.com](https://www.kasparov.com/timeline-event/deep-blue/).*

## Deliverables due and in-class quiz on 3/13

## Overview

A *game*, in the theoretical sense, is a strategic interaction. *Game theory* is the branch of mathematics and economics that studies the properties of strategic games and investigates when and how good strategies exist for players. Our typical model of a game is something like chess, or a similar board game: two players, alternating turns, with deterministic rules and visible game state. We can create many variations on this basic concept:

- Most board games are *zero-sum*, where every win is balanced by a loss, but cooperative and non-zero-sum games exist.
- Turns can be alternating or simultaneous.
- Outcomes can be deterministic or stochastic
- Information can be *perfect*, where the entire state of the game is known to the players (like in chess), or *imperfect*, where some information is concealed (as in poker)

This unit extends the search concept to **adversarial search**. We'll now consider optimal planning for sequential two-player games, where each player is trying to make the best possible moves. The main algorithm for this unit is the *minimax algorithm*, which implements tree search under the assumption that players are making rational and optimal moves.

Game playing has been a driver of innovation in artficial intelligence since the early days. Christopher Strachey wrote an [implementation of checkers](https://en.wikipedia.org/wiki/Checkers_(video_game)) in 1952 with a primitive AI that may have been the first video game with graphics. Chess emerged as a major research focus from the 1970s until Kasparov's loss to Deep Blue, after which the community switched to the Asian game of go. Major wins at go were achieved by Google DeepMind's AlphaGo in 2016, which managed to defeat the top-rated pro player Lee Seidol using a combination of machine learning and an algorithm called *Monte Carlo Tree Search*.

## Topics

- The minimax concept
- The recursive minimax implementation
- Alpha-beta pruning
- Multi-armed bandits and the UCB1 heuristic
- Monte Carlo Tree Search

Most of the work in this unit is implementing your own original game program. See the deliverable description.

## Resources

The algorithms are pretty straightforward. Use the Notes directory to get started and then review the [chapter on Games](https://inst.eecs.berkeley.edu/~cs188/textbook/games/) in the Berkeley text.
