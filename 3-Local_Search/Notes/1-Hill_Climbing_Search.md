# Hill Climbing Search

## Local search

Our previous units considered variations on tree search. All of the various algorithms we studied - BFS, DFS, A*, etc. - maintained a tree of states in memory and explored the space of problem states in a structured way. These algorithms could be complete and optimal and also allowed us to reconstruct the sequence of states from the start to the goal.

However, memory requirements can be an issue for tree search. We dealt with this, to some extent, by choosing methods like iterative deepening that had low memory overhead.

Consider, however, that some problems may not have a specific goal state, but still have a way of assessing the quality of a solution. These are *optimization* problems, where the goal is to find the parameters that maximize some **objective function**. 

The **local search** approach begins with a starting state, which might be randomly initialized, and then moves to a neighbor state. We continue this process, moving from neighbor to neighbor, until the method either reaches an optimal objective value or becomes stuck and can't make further progress. Local search methods can be applied to optimization problems where the goal is to maximize (or minimize) an objective. Their memory requirements are usually *O*(1); only one state at a time needs to be kept in memory.

## Local and global maxima

<img src="https://inst.eecs.berkeley.edu/~cs188/textbook/assets/images/maxima_global_local.png" width="500px" />

*From the Russell and Norvig book and the online Berkeley text*

The figure shows an example continuous objective function with a several peaks. The goal of a search method is to find the *global maximum*, the point with the overall highest objective value. A *local maximum* is characterized by a neighborhood (which might be arbitrarily small) where it's the best value.
> Question: is a global maximum also a local maximum?

The same concepts apply to minimization. Note that if we have the objective function $$f(x)$$,

$$ \max_x f(x) = -\min_x f(x) $$

and vice-versa.

Not every function has a maximizer or minimizer - for example, *f*(*x*) = *e*<sup>*x*</sup>. A function like *f*(*x*) = sin *x* has infinitely many global maxima and minima.

As the figure shows, the basic challenge of local search is that it's impossible to determine if a maximum is really a global maximizer or only a local maximum. Unless you have extra information about the problem, you generally can't tell. Also observe that local methods can get confused by features like plateaus and ridges in objective space.\

## Running up that hill

The simplest local search method is **hill climbing**, or *steepest ascent**. At each, step move to the neighbor state with the highest objective value. Continue making moves until no further ascent is possible, then stop.
```
Hill climbing search

input:
    objective function f(x)
    the starting state

output:
    a local maximizing state

// Initialize starting state
s = starting_state

// Hill-climbing loop
while (true) {

    neighbor = successor of s with highest f(x) value

    // Stopping condition: no more upward progress is possible
    if f(neighbor) <= f(s) {
        return s
    }

    # Move up the hill
    s = neighbor
}
```
The main loop checks the neighbors of *s* and keeps the one with the highest objective. If that neighbor is better than *s*, move to it. Otherwise, the search has reached a local maximum and it's time to stop.

## Example: 0/1 knapsack

Suppose we want to apply hill climbing to the following knapsack problem:
```
capacity = 10

Item   Weight   Value
----   ------   -----
 1        2       10
 2        3       15
 3        5       15
 4        7       20
```
Let the starting state be an empty knapsack: `[0, 0, 0, 0]`. The first iteration generates the neighbor states and scores each one. If we define neighbor to mean a state that's one bit flip away, there are four options:

- `[1, 0, 0, 0]`, which has a value of 10
- `[0, 1, 0, 0]`, which has a value of 15
- `[0, 0, 1, 0]`, also with 15
- `[0, 0, 0, 1]`, with a value of 20

The best neighbor is `[0, 0, 0, 1]`, so the method moves there. The second iteration will generate the successors of that state and discover that `[0, 1, 0, 1]` is the best option with a score of 35. The method then terminates: there are no more items that can fit in the knapsack.

So pure hill climbing finds a solution with value 35. The true optimal solution is `[1, 1, 1, 0]` with a value of 40.
> Try starting from a different state and see what results you get.

This example is simple but illustrates some of the challenges of local search:

- Methods are sensitive to the initial conditions. Small differences in the start can lead to radically different paths and outcomes.
- The requirement to always move up can lead to getting blocked

## Variations

It's easy to come up with some variations that might make hill climbing better. For example,

- Don't always take the steepest upward move. Maybe pick a random move from among the set of uphill moves.
- Try randomly restarting from different locations
- Rather than enumerating all successors, generate them randomly until you find a better one; this is useful if a state has a huge number of successors
- *Maybe*, just maybe, we could allow some sideways, or even downward, moves to help break out of local minima or off of plateaus?
