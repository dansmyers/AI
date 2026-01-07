# Uniform Cost Search

<img src="../Images/florida_cities.png" width="600px" />

## Overview

Let's return to our earlier example of finding routes between cities in Florida.

So far, we've only considered *finding* a plan - any plan - that achieves the goal state. Our default behavior has been to stop the search process as soon as we reach the goal. For some problems this is sufficient. We've also seen how breadth-first and iterative deepening searches will always find a solution that is the minimum number of state transitions away from the starting state.

Recall, from note #1, that some problems incorporate a cost function, where `cost(s, a)` returns the cost of taking action `a` in state `s`. For the map example, the cost naturally corresponds to the difference between cities; for example, `cost(Gainesville, Orlando)` is 

In some cases, like the map example, we probably want the *minimum cost plan*. That is, we'd like a plan that minimizes the cost of the actions taken 
