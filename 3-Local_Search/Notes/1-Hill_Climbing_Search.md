# Hill Climbing Search

## Local search

Our previous units considered variations on tree search. All of the various algorithms we studied - BFS, DFS, A*, etc. - maintained a tree of states in memory and explored the space of problem states in a structured way. These algorithms could be complete and optimal and also allowed us to reconstruct the sequence of states from the start to the goal.

However, memory requirements can be an issue for tree search. We dealt with this, to some extent, by choosing methods like iterative deepening that had low memory overhead.

Consider, however, that some problems may not have a specific goal state, but still have a way of assessing the quality of a solution. These are *optimization* problems, where the goal is to find the parameters that maximize some **objective function**. 

The **local search** approach begins with a starting state, which might be randomly initialized, and then moves to a neighbor state. We continue this process, moving from neighbor to neighbor, until the method either reaches an optimal objective value or becomes stuck and can't make further progress. Local search methods can be applied to optimization problems where the goal is to maximize (or minimize) an objective. Their memory requirements are usually *O*(1); only one state at a time needs to be kept in memory.

## Local and global maxima

<img src="https://inst.eecs.berkeley.edu/~cs188/textbook/assets/images/maxima_global_local.png" width="400px" />

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
