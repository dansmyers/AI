# Iterative Deepening

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/View_down_the_Well.jpg/960px-View_down_the_Well.jpg" width="600px" />


*The Initiation Well of the [Quinta de Regaleira](https://en.wikipedia.org/wiki/Quinta_da_Regaleira) palace in Sinta, Portugal. The palace and its surrounding estate were constructed in the early 1900s by the wealthy and eccentric Portuguese businessman Carvalho Monteiro, who filled the property with Romantic architecture and symbolism related to Freemasonry, the Knights Templar, and esoteric philosophy. The "well" is one of two on the property and is constructed like an inverted tower, descending nine levels. The floor at the bottom is inlaid with a Templar cross. Image by Wikipedia user Stijndon.*

## Overview

Recall that depth-first search selects one solution path and explores it to completion, then moves to the next deepest path, and so forth. This process works well if it's easy for the method to find a path that leads to a solution, which is true for many problems. But it also runs the risk of becoming stuck on a deep path that never leads to a solution.

A *depth-limited search* solves the problem of arbitrarily deep search paths. The strategy is simple: Keep track of the depth of each node in the current search tree and don't expand nodes beyond a set max depth. Of course, this method may fail if no solution exists within the chosen max search depth.

The **iterative deepening** approach performs sequential depth-limited searches:

- Start with a max depth of 0, which is the root. If the root isn't the solution, this search fails.
- Increase the max depth to 1, which corresponds to the first level of the search tree. If the solution doesn't exist on the first level, this search fails.
- Increase the limit to 2 to check nodes up to the second level of the search tree.
- Continue this process, increasing the max depth one level at a time to expand the search deeper into the tree until you eventually find a solution.

Each iteration begins a new depth first search from the root, but is allowed to descend one layer deeper into the tree.

This approach has good properties of both breadth- and depth-first search:

- The memory requirements scale like DFS, since there is still only one primary search path at any moment
- Like BFS, the method terminates with the solution that is the minimum number of levels from the root

## Pseudocode




