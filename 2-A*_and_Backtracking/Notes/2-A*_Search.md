# A* Search

## Overview

The A* search algorithm combines the main ideas of the uniform cost and greedy search algorithms. Consider a node *n* in the search tree.

- Let *g*(*n*) be the cumulative path cost to reach node *n* from the root
- Let *h*(*n*) be the heuristic estimate of the distance from *n* to the solution

The A* algorithm calculates the total cost of *n* as the sum of both costs:

$$ f(n) = g(n) + h(n) $$

That is, A* estimates the cost of a node as being the cost to *reach* node plus the *estimated remaining cost* to the solution. At each step, A* expands the node with the lowest value of *f*(*n*).

The name A* comes from a 1968 paper by Peter Hart, Nils Nilsson, and Bertram Raphael. The name comes from the notation used in their paper. They described a series of algorithms—A₁, A₂, etc.—with increasing levels of information used to guide the search. A* represented the algorithm that used the optimal amount of heuristic information, making it the "best" version in the class.

## Properties

A* search is the "best" tree search algorithm, provided that the heuristic has the property of **admissibility**, discussed below.

- A* is *complete*: It's guaranteed to find a solution if one exists
  
- It's also *optimal*: It will find the solution path of minimum cost. Uniform cost search also had this property without using a heuristic
  
- If the actual optimal cost to reach the solution is some value *C*, then A* will expand nodes with value *f*(*n*) < *C*. It turns out that every other optimal algorithm using the same heuristic information must also expand these nodes before reaching the solution. A* is no worse than any other method that can find the optimal solution using the same amount of information, in terms of the set of nodes it is required to expand.

## Admissibility

Optimality of A* requires that the heuristic be *admissible*. Let *h**(*n*) be the real distance from *n* to the solution. The heuristic *h* is admissible if, for all nodes *n*,

$$ 0 \leq h(n) \leq h*(n) $$

That is, the heuristic *h*(*n*) can't be negative and always **underestimates** the true distance to the solution. Intuitively, making the heuristic underestimate the true distance makes every value of *f*(*n*) a *lower bound* on the total cost to reach the solution.

The A* method always expands the node at the current known lowest bound estimate.

Note that for the goal state *g*, we're required to have *h*(*g*) = 0.

## Pseudocode

```
A* Search

input:
    initial state i
    goal state g
    successors function      // returns (successor, edge_cost) pairs
    heuristic function h     // estimates cost from any state to goal

output:
    success if the goal state is reachable, failure otherwise

initialize empty priority queue frontier (ordered by f value, lowest first)

// g[x] = cost of best known path from i to x
// f[x] = g[x] + h(x) = estimated total cost through x

g[i] = 0
f[i] = h(i)

// Begin with the starting state
frontier.insert(i, priority = f[i])

while frontier is not empty {

    // Choose the state with lowest f value
    x = frontier.pop()

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

    // Insert new successor states into frontier with updated costs
    for (j, cost) in s {

        tentative_g = g[x] + cost

        // Only consider this path if it's better than any known path to j
        if tentative_g < g[j] (or g[j] is undefined) {
            g[j] = tentative_g
            f[j] = g[j] + h(j)
            frontier.insert(j, priority = f[j])
        }
    }
}

// If the loop ends, the state space was exhausted without reaching the goal
output failure and stop
```
