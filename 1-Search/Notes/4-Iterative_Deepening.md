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

## The number of nodes

It might seem like the iterative process is wasteful, because you end up repeatedly re-searching the lower levels of the tree until you finally hit the appropriate max depth. It turns out, however, that this is not a major problem.

Here's an important point about balanced trees: **most of the nodes are at the bottom level**.

Suppose you have a perfect binary tree (one where every level is full and there are no missing nodes) with a height of *d*. That is, there are *d* levels below the root.

- Level 0 is 1 node, the root (recall that the root is considered level 0)
- Level 1 has 2 nodes
- Level 2 has 4 nodes
- Level 3 has 8 nodes, and so forth

The bottom level, *d*, has 2<sup>*d*</sup> nodes.

The total number of nodes in the tree is:

$$ 1 + 2 + 4 + 8 + \dots + 2^d = 2^{d + 1} - 1 $$

So approximately half the nodes are on the bottom level, which means that about half of the work of the search only happens on the final iteration. If *b* is the branching factor and *d* is the depth of the solution, then the complexity of iterative deepening (in terms of the total number of nodes examined) is *O*(*b*<sup>*d*</sup>).

Here's a subtle but important point. If the solution lies at depth *d*, a standard breadth-first search will still expand the nodes at level *d*, which creates new nodes at level *d + 1* These are unnecessary, since the solution occurs at *d*, but the method has no way of knowing that as it executes. Iterative deepening will explore the nodes at *d* **without expanding them** and find the solution without creating any unnecessary nodes.

This more than makes up for the overhead of repeatedly searching the lower levels of the tree, such that ID is actually faster than BFS.

According to Russelland Norvig, **Iterative deepening is the preferrred uninformed search method when the search space is large and the depth of the solution is unknown.**

## Pseudocode

```
Iterative Deepening Tree Search

input:
    initial state i
    goal state g
    successors function

output:
    success if the goal state is reachable, failure otherwise

// Outer loop: progressively increase depth limit
for depth_limit = 0 to infinity {

    initialize empty frontier stack
    visited = set()

    // Begin with the starting state at depth 0
    frontier.push((i, 0))  // (state, depth)

    while frontier is not empty {

        // Choose the next state to expand
        (x, depth) = frontier.pop()

        // If x is the goal state, we're done
        if x == g {
            output success and stop
        }

        // Don't expand already visited states
        if visited[x] {
            continue
        }

        // x is now being visited, so mark it
        visited[x] = True

        // Only expand if we haven't reached the depth limit
        if depth < depth_limit {

            // Generate successors of x
            s = successors(x)

            // Insert successor states into frontier
            for j in s {
                frontier.push((j, depth + 1))
            }
        }
    }
    
    // Current depth exhausted; try deeper
}

// If no solution exists at any depth
output failure and stop
```




