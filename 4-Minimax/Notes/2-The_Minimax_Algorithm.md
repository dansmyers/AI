# The Minimax Algorithm

The previous note introduced the concepts of adversarial search and the idea of the game tree. By playing out the sequence of moves, counter-moves, counter-counter moves and so forth, a player could choose the top-level action that yielded the best outcome. This was done with the assumption that the opposing player behaved *rationally* and sought to maximize their own outcome.

We formalized this into the minimax concept: On my turn, I should choose the move that *maximizes* my score in the resulting game subtree, under the assumption that my opponent will play to *minimize* my score in each subtree.

##  An abstract game tree

<img src="Images/minimax_game_tree.png" width="500px" />

The image above shows an **abstract game tree** illustrating the minimax concept. The upward and downward triangles represent move choices made by the maximizing and minimizing player, respectively. The leaves represent outcomes, with scores for each outcome. We don't have to care what the moves or scores represent in this tree, only that it alternates levels of minimizing and maximizing.

Consider the bottom-left subtree, with leaves of 5 and 6. The maximizing player seeks the greatest score, so given a choice between those two outcomes, he'll choose the move that yields 6. Likewise, in the next subtree, he'll compare the two outcomes of 9 and 7 and choose the move yielding 9. The bottom max level shows the best outcome the maximizing player can obtain from each pair of leaves.

The minimizing player will always select the move that yields the minimum score through its subtree, under the assumption that the opponent is playing to maximize. The leftmost branch offer the minimizer a choice of a subtree with a best score of 6, or one with 9: the minimizer chooses the move that will guarantee a 6. The rightmost tree offers choices that lead to outcomes of 10 and 5. The minimizer rationally chooses the 5 option. Examine the middle branch and verify that the best option for the minimizer is a score of 4.

At the root, the maximizer chooses from among the three branches. The best choice is the left branch, because it offers the highest score taking into account the minimizer's choices. Therefore, the best outcome the maximizer can obtain in this tree is 6.

## Pseudocode

The minimax algorithm is implemented recursively. The basic strategy is to use a variable `is_max_player` that tracks whether this level of the search corresponds to a minimizing or maximizing player. The method also uses a `depth` parameter to prevent the search from going too long. We'll discuss managing the size of the game tree in more detail later.

```
Minimax Algorithm

minimax(node, depth, is_max_player) {

    // Base case: finishing state or search exhausted
    if depth == 0 or node is a finishing state {
        return score(node)
    }

    // Maximizing choice
    if is_max_player {
        best = -infinity
        for each child of node {
            value = minimax(child, depth - 1, false)
            best = max(best, value)
        }
    }

    // Minimizing choice
    else {
        best = +infinity
        for each child of node {
            value = minimax(child, depth - 1, true)
            best = min(best, value)
        }    
    }

    return best
}
```

## The evaluation function

A naive version of minimax would require playing out *the full game tree* for every possible move to reach and score every terminating state. Unless a game is small, this probably isn't feasible.

The depth-limited version shown above will prevent the search from branching out of control, but there are two issues that need to be considered:

1. What is a good choice for the initial value of `depth`, which determines the number of levels in the tree? There's no fixed rule. In general, you should probably run the deepest possible search that you can without making moves take too long.

2. More seriously, what should we do about incomplete states? If `depth` reaches 0, we probably won't be in a terminal state, so we can't simply score a win or loss.

Consider chess. It's almost always infeasible to play out a full game tree for chess, so most minimax searches will end on some intermediate board state. The `score` function then becomes an assessment of how good that board state is for the current player. For example, if it's white's turn, then outcomes that place white in a strong position should be favored, because those are more likely to lead to wins than states that give black the dominant board position.

The *evaluation function* takes a state and returns an approximation of its minimax score. This function allows us to evaluate the quality of incomplete states: a state with a high evaluation is closer to a winning state for the maximzing player, and likewise for low evaluations and the minimizing player.

## Example: material scoring in chess

A standard form for evaluation functions is to take a linear combination (that is, a weighted sum) of features.

All chess engines use *material scoring* as a basic part of their board evaluation functions. Each piece is assigned a weight approximating how strong it is. One standard weighting system is the following:

- 1 point for each pawn
- 3 points for each knight and each bishop
- 5 points for each rook
- 9 points for each queen

The strength of a player's position is the sum of the points for their remaining pieces.  For example, if white has 5 pawns, 1 bishop, 1 knight, and 2 rooks remaining, its score would be 21 points. The relative strength of white's position is found by calculating its score difference compared to black:

$$ score_{wh} = (P_{wh} - P_{bl}) + 3(K_w - K_{bl}) + 3(B_{wh} - B_{bl}) + 5(R_{wh} - R_{bl}) +  9(Q_{wh} - Q_{bl}) $$

More complex versions will consider not just the number of pieces, but also add or remove points for pieces that are in strong positions vs. weak positions. For example, knights are stronger in the center of the board than on the edges and pawns are in a better position when advanced. You can also incorporate information on the phase of the game (early, mid, or end), which can impact positional valuation.

See [this article](https://chessify.me/blog/chess-engine-evaluation) for more information on chess evaluation design.

In practice, much of the work of a real game-playing minimax engine is in designing a good evaluation function that captures the important strategic elements of the game. In recent years, many programs have moved to using neural networks to learn evaluations from data. This was a key element in the AlphaGo program that we'll discuss in a future note.
