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

Let's consider a heuristic for the grid-based motion planning problem. A basic strategy for designing heuristics is to **relax the constraints**. Imagine that the grid world had no walls: then you could just move directly to the solution without having to go around any barriers.

Therefore, let's define the heuristic as follows. Let (*g*<sub>*x*</sub>, *g*<sub>*y*</sub>) be the coordinates of the goal and (*r*<sub>*x*</sub>, *r*<sub>*y*</sub>) be the coordinates of the robot. The heuristic is the sum of the horizontal and vertical distances from the robot to the goal:

$$h(x, y) = |g_x - r_x| + |g_y - r_y|$$ 

## 
