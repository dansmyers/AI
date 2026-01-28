# Informed Search and Heuristics


## Motion planning

Here's a standard problem that we'll use to motivate much of the discussion in this unit. Suppose that we have a robot that needs to navigate through a grid-based world to reach a marked destination square, where there are obstacles that might impede movement. Here's an example where the starting position is marked with `O`, the destination is `X`, the obstacles are `#` symbols, and the shortest path is marked in dots:
```
##############################
#O.........           #      #
#    #####.           #      #
#####   ...           ########
#       .###############     #
#       .....                #
#     ######.                #
#           .                #
#           ................X#
##############################
```

Let's think about how our different search algorithms would deal with this problem:

- Breadth-first search would start by exploring all squares that are one move away from the start, then all squares that are two moves away, and so forth. It's guaranteed to find the path to the solution in the minimum number of moves, but will end up expanding a lot of unnecessary nodes because it has no way to prioritize the direction of the search.

- Depth-first search will pick a direction and explore it to completion, then back up to choose the next closest path and explore that to completion, and so forth. Its performance on this problem is difficult to predict. It might be very fast if the initial direction it chooses moves toward the solution. Pure DFS isn't guaranteed to find the optimal solution.

- Uniform-cost search behaves like BFS on this problem, beacuse the cost of every move is equal and the total cost of a path is the number of moves it contains. A variation would add "terrain" to make some squares more expensive to move onto than others, so the shortest cost path might not be the one with the minimum number of steps.

There's something missing in all of these approaches. Intuitively, we'd like the search to prioritize *moving toward the solution*. This is the basis of **informed search**.

An informed search algorithm uses a **heuristic** function to estimate the distance to the solution. Formally,

- Let *n* be a node in the search tree
- The heuristic function *h*(*n*) returns an estimate of the distance to the goal state from *n*

Notice that for the goal state *g*, we're required to have *h*(*g*) = 0 by the definition - the distance from the goal to itself must be 0.

We'll also have to define (in the next note), some properties that make a heuristic function useful. It's easy to realize that the heuristic needs to have some underlying relationship to the real distance if it's going to be useful.

## Manhattan distance

Let's consider a heuristic for the grid-based motion planning problem. A basic strategy for designing heuristics is to **relax the constraints**. That is, think about how you could easily solve the problem if your choices weren't restricted. That approach is guaranteed to give you a *lower bound* on the real cost to reach the solution.

Imagine that you could ignore the walls in the grid world: then you could just move directly to the solution without having to go around any barriers. The shortest path would be the direct horizontal and vertical lines that connect the start to the destination.

Therefore, let's define the heuristic as follows. Let (*g*<sub>*x*</sub>, *g*<sub>*y*</sub>) be the coordinates of the goal and (*r*<sub>*x*</sub>, *r*<sub>*y*</sub>) be the coordinates of the robot. The heuristic is the sum of the absolute horizontal and vertical distances from the robot to the goal:

$$h(r_x, r_y) = |g_x - r_x| + |g_y - r_y|$$ 

This is called the **Manhattan distance**, or *city-block distance*, because it measures the distance between two points in terms of their horizontal and vertical distance on a grid.

Here's a visual example. Normally `O` would have to go around the walls, but the heuristic allows you to consider the shortest path as if the walls didn't exist. The `/` denotes places where the direct path cuts through walls.
```
##############################
#                     #      #
#    #####            #      #
#####      O          ########
#        ##/############     #
#          .                 #
#     #####/                 #
#          .                 #
#        X..                 #
##############################
```
The Manhattan distance from `O` to `X` is 7 moves.

### Some heuristics are better than others

You could choose to relax the constraints by letting the robot immediately jump to the target in 1 move. This would be equivalent to a function *h*(*n*) = 1 for all *n* that aren't the goal state.

This is a valid heuristic, in the sense that it gives a lower bound on the real cost to reach the solution, but it's not a *useful* one. Every state has the same heuristic cost, so the function gives you no information to prioritize one path over another.

The "jump to the solution" heuristic is *a* lower bound, but it's a very weak lower bound compared to the city-block distance. If a problem admits multiple choices of heuristics, we're going to prefer the one that gives the *tightest* possible lower bound; that is, the one that gives results closest to the true path cost.


## Greedy search

Our first informed search algorithm is **greedy search**. At each step, greedy search chooses to expand the node with the minimum heuristic distance to the goal. Intuitively, it picks what seems to be the most promising solution path at each step. 

Greedy search is *forward looking*. It doesn't consider the accumulated cost to reach a state, only the estimated distance to reach the goal; it always tries to take the step that *appears* to move most aggressively toward the goal. Uniform-cost search, by contrast, was backward looking: it always expanded the node with the minimum distance from the start.

On some problems, greedy search can perform well. If the heuristic reliably guides the algorithm towards the goal, it will probably find a good path without expanding very many extra nodes. However,

- Greedy search isn't guaranteed to find the optimal solution
- It can perform like a bad DFS, where it gets lost on unproductive paths

We'd like to have method that uses a heuristic to guide the search, but offers better guarantees than pure greedy search. The next note decribes the algorithm that does exactly that: **A\* search**.
