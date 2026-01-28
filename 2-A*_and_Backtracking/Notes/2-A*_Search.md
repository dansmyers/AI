# A* Search

## Overview

The A* search algorithm combines the main ideas of the uniform cost and greedy search algorithms. Consider a node *n* in the search tree.

- Let *g*(*n*) be the cumulative path cost to reach node *n* from the root
- Let *h*(*n*) be the heuristic estimate of the distance from *n* to the solution

The A* algorithm calculates the total cost of *n* as the sum of both costs:

$$ f(n) = g(n) + h(n) $$
