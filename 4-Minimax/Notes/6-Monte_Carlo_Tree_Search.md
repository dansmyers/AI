# Monte Carlo Tree Search

<img src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/AlphaGo_hero.width-2200.format-webp.webp" width="500px" />

*Lee Sedol vs. AlphaGo in 2016. After Deep Blue's defeat of Kasparov, the AI community discovered that winning at chess was **not** the end of intelligence research and searched for a new game to adopt as a major open problem. Go emerged as the next major frontier in game-playing AI. Go is played on a 19x19 grid between two players who place white and black stones. The object is to place your stones in a way that captures your opponent's stones and controls the most territory at the end of the game. Go is harder for AI than chess because the branching factor is much higher (there may be hundreds of possible moves at each turn) and because estimating the quality of a move is more difficult. The strategic value of a position may not become clear until many turns later, so standard minimax-based search struggles to identify good moves. Google achieved a major breakthrough with the AlphaGo program, which beat the world's top player Lee Sedol in 2016.*

## Overview

The core problem of classical minimax is the need to expand the (potentially huge) game tree. Even with pruning and evaluation functions, this my be impractical if the game has a high branching factor.

**Monte Carlo Tree Search** (MCTS) is a variation of minimax that uses *random sampling* to estimate the outcome of paths in the game tree, rather than exhaustive expansion. *Monte Carlo simulation* refers to a general category of algorithms that use samples to estimate complex calculations that would be impossible or inconvenient evaluate exactly. The name comes from the Monte Carlo casino complex in Monaco.

Intuitively, the method samples random paths through the game tree. Repeatedly play out a full game from root to a leaf (usually by picking random moves on each step) and record the result in the leaf. At the end, pick the top-level move that yielded the highest fraction of wins among its descendant leaves.

If you think about it, this is a variation of the multi-armed bandit problem:

- The top level moves are like arms on the slot machines

- Choosing a particular top-level move and playing out that game gives you information about its effectiveness

- There is an explore vs. exploit tradeoff: you need to test enough to learn whether a branch is good, but you also want to quickly discard unpromising branches


