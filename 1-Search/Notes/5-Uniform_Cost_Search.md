# Uniform-Cost Search

<img src="../Images/florida_cities.png" width="400px" />

## Overview

Let's return to our earlier example of finding routes between cities in Florida.

So far, we've only considered *finding* a plan - any plan - that achieves the goal state. Our default behavior has been to stop the search process as soon as we reach the goal. For some problems this is sufficient. We've also seen how breadth-first and iterative deepening searches will always find a solution that is the minimum number of state transitions away from the starting state.

Recall, from note #1, that some problems incorporate a `cost` function returns the cost of taking action `a` in state `s`. The cost captures how difficult or expensive a certain action is for the particular state. For the map example, the cost naturally corresponds to the difference between cities; for example, `cost(Gainesville, go to Orlando)` is 110.

If a cost function exists for a problem, we typically want the *minimum cost plan* that minimizes the total cost of the actions taken while moving from the initial state to the goal state.

The **uniform-cost search** modifies the basic algorithm in two ways:

- Keep track of the total cost to reach each node in the search tree. For example, suppose you're considering a state that represents the route Tallahassee-Gainesville-Orlando. The total distance of that route is 240. Call this the *path cost* of the node.

- When expanding nodes, always choose the **node with the lowest path cost**. This requires using a priority queue data structure sorted by path cost, so that popping from the queue always returns the node of minimum value.

## Pseudocode

The basic approach shown below should be familiar by this point. This version assumes that the `successors` function calculates the incremental step cost of moving to each successor state and returns its results as a `(state, step cost)` tuple.

```
Uniform Cost Search

input:
    initial state i
    goal state g
    successors function  // returns list of (next state, step cost) tuples

output:
    success if the goal state is reachable, failure otherwise

initialize empty priority queue frontier (ordered by cost, lowest first)

// Begin with the starting state at cost 0
frontier.insert(i, 0)

while frontier is not empty {

    // Choose the state with the lowest cumulative cost
    (x, cost) = frontier.pop_min()

    // If x is the goal state, we're done
    if x == g {
        output success and stop
    }

    // Check if x has already been visited; if so, don't expand it again
    if visited[x] {
        continue
    }

    // We're now visiting x, so mark it
    visited[x] = True

    // Generate successors of x
    s = successors(x)

    // Insert new unvisited successor states into frontier with cumulative cost
    for (j, step_cost) in s {
        if not visited[j] {
            frontier.insert(j, cost + step_cost)
        }
    }
}

// If the loop ends, the state space was exhausted without reaching the goal
output failure and stop

```


