# Alpha-Beta Pruning

## Overview

The vanilla minimax algorithm builds the game tree by expanding all possible moves and counter-moves down to a pre-set maximum depth. A good evaluation function helps estimate the quality of moves when the depth is too shallow to play out the full tree, but this procedure might still end up generating an impractically large number of nodes.

However, it's often possible to speed up the search by **pruning** subtrees that can provably never affect the result. The main pruning algorithm for minimax is **alpha-beta pruning**.

## Example

<img src="Images/minimax_prune.png" width="400px" />

The figure above shows the abstract game tree from the previous note in a partially complete state. Observe the following:

- The left subtree has been evaluated, yielding a value of 6 through its min node

- The root node is therefore guaranteed to achieve a result of **at least** 6 through its left subtree. There might be a better result available through one of the other subtrees - we don't know yet!

- The central subtree is partially evaluated. The min node there has identified a value of 4 through its left subtree. Therefore, this node is guaranteed a result of **at most** 4. There might be a lower value available through the other subtree, but the min node won't select it yields a value lower than 4.

Now think about the relationship between the root and the cental min node. The root wants to maximize and is guaranteed at least 6, via the result from its left subtree. The central min node will return **at most**, so the root is guaranteed to reject its value. Therefore, *there's no reason to explore the second subtree of the central branch.*

## Algorithm

The example illustrates one half of the pruning strategy:

- When processing a min node, keep track of the best values known to its ancestor max nodes

- Once the min node identifies a result *less than* the best result known by any of its higher-level max nodes, it can stop exploring subtrees and return immediately. In our example, the min node identified a value of 4, which was less than the 6 known to a higher-level max node, so the min node is guaranteed to return a result that won't be accepted.

Max nodes use the same strategy with the roles of the nodes reversed. For every max node, keep track of the best results known to its ancestor min nodes. When a max node identifies a result *greater than* the best results known to its higher-level min nodes, then it can stop exploring subtrees and return immediately. The max node is therefore guaranteed to return a result that won't be accepted by the min node.

The **alpha-beta pruning** algorithm keeps track of two parameters as it builds the game tree. For each node,

- `alpha` is the largest value identified by the max nodes on the path to the root
- `beta` is the smallest value identified by the min nodes on the path to the root

It may be helpful to think of `alpha` as the max player's current best known result. It would be good (for the max player) if it can continue to identify even larger values that represent better outcomes, but `alpha` represents the lower bound that it's guaranteed to achieve even if no more nodes are explored. Likewise, `beta` is the current estimate of the min player's best outcome.

For a max node, return immediately once you have identified a score ≥ `beta`. These represent choices that are no better (for the min player) than what it can already obtain through a previously identified path.

For a min node, like the one in the example, return immediately if you identify a score ≤ `alpha`. Again, this represents a value that is no better than what the max player can already obtain.

## Pseudocode

