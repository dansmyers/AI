# Maintaining the History of the Search

## Overview

We know how to use search to explore a search tree and find the goal state. We also know how to use uniform-cost search to find a solution with minimum total cost. However, we've only considered *discovering* that the solution exists. We also need to **return the sequence of states** on the solution path, so we can construct the plan of actions that moves from the start state to the goal.

The strategy is to use an additional structure to keep track of the **parent** of each node in the search tree. When we create the successors of a node, we'll include the parent state as part of the node's information. Then, when a node is marked as visited, record its official parent in the map. When we reach the goal, we can then recover the sequence of intermediate states by following the chain of parents backwards to the start.

## Pseudocode

```
Uniform Cost Search with Path Tracking

input:
    initial state i
    goal state g
    successors function  // returns list of (next state, step cost) tuples

output:
    path from i to g if reachable, failure otherwise

initialize empty priority queue frontier (ordered by cost, lowest first)
initialize empty map parent  // maps each state to its predecessor

// Begin with the starting state at cost 0, no parent
frontier.insert(i, null, 0)

while frontier is not empty {

    // Choose the state with the lowest cumulative cost
    (x, x_parent, cost) = frontier.pop_min()

    // Check if x has already been visited; if so, don't expand it again
    if visited[x] {
        continue
    }

    // We're now visiting x, so mark it and record its true parent
    visited[x] = True
    parent[x] = x_parent

    // If x is the goal state, reconstruct and return the path
    if x == g {
        path = reconstruct_path(x, parent)
        output path and stop
    }

    // Generate successors of x
    s = successors(x)

    // Insert successor states into frontier with cumulative cost
    //
    // x is included as the parent of j
    for (j, step_cost) in s {
        frontier.insert(j, x, cost + step_cost)
    }
}

// If the loop ends, the state space was exhausted without reaching the goal
output failure and stop
```

The `reconstruct_path` function works backwards through the `parent` structure:
```
reconstruct_path(goal, parent) {
    path = []
    current = goal
    
    while current is not null {
        path.prepend(current)
        current = parent[current]
    }
    
    return path
}
```

## Example: the eight-puzzle

<img src="https://www.aiai.ed.ac.uk/~gwickler/images/8-puzzle-states.png" width="400px"/>

*From [The Artificial Intelligence Applications Institute](https://www.aiai.ed.ac.uk/~gwickler/eightpuzzle-uninf.html). Follow the link for a playable version.*

The eight-puzzle is sliding block game using a 3x3 grid. There are eight tiles numbered 1-8, and one tile missing. The goal is slide the blocks and arrange the numbers in sorted order. It's a classic AI search demonstration problem. Larger variants with 15 or more blocks exist.


