# Breadth-First and Depth-First Search

## Overview

The previous note discussed the basic strategy of state-space search for solving planning problems: given an initial state, explore the search tree until you find a sequence of actions leading to the goal state. We were vague, though, on how to practically implement this strategy for a real problem.

We're going to look at the two canonical search algorithms: breadth-first and depth-first search (BFS and DFS), which are really almost the same method. These are standard techniques that show up again and again throughout computer science in a variety of different contexts, including path finding in networks, graph analysis, and game playing. By themselves, BFS and DFS may not be suitable for every problem, but they're still the building blocks of more advanced techniques.

Make sure you've reviewed the previous material, particularly the pseudocode for tree search before continuing with this note.

## Breadth-first search

Recall that the tree search method uses a data structure called `frontier` to maintain the set of known but still unexpanded search tree nodes. The breadth-first search algorithm uses a **first-in-first-out queue** as the frontier structure. At each step, it chooses the *oldest* known node (that is, the node that was identified earliest in the search process) and expands it.

Consider the following abstract map of some major cities in Florida. The edges represent approximate routes.

<img src="../Images/florida_cities.png" width="400px" />

*Made with Claude Opus 4.5. Everything is approximate. This is inspired by a similar example in Russell and Norvig's classic book Artificial Intelligence: A Modern Approach that used a map of cities in Romania.*

Suppose we want to plan a route from Tallahassee to Miami. In this problem, a state is a city in the map and an action corresponds to moving from a city to one of its neighbors.

At the beginning of the algorithm, place Tallahassee into the queue as the starting node.
```
[Tallahassee]
```
The first step removes Tallahassee from the queue and expands its successor states, which are Gainesville, Pensacola, and Jacksonville. These are inserted into the queue:
```
[Gainesville, Pensacola, Jacksonville]
```
From a search tree persepctive, we've constructed the following:
```
                   Tallahassee
                        |
                        |
         -----------------------------
        |               |             |
    Gainesville     Pensacola    Jacksonville
```
The next step removes the first item in the queue, which is Gainesville, and expands it to reach Orlando and Tampa. The queue and search tree now look like the following:
```
[Pensacola, Jacksonville, Orlando, Tampa]
```
```
                   Tallahassee
                        |
                        |
         -----------------------------
        |               |             |
    Gainesville     Pensacola    Jacksonville
        |
        |
    --------- 
   |         |
Orlando    Tampa
```

### Practice question

> What will happen on the next iteration? Which node is expanded next?

The BFS algorithm always takes the next unexpanded node at the front of its queue, so the next visited city will be **Pensacola**, followed by Jacksonville, then Orlando, and so forth.

The breadth-first search algorithm gets its name because it explores the search tree in *level-order*. After the root, all nodes on the first level are expanded before moving to the second level, which is then fully explored before moving to the third level, and so forth. Nodes on each level are expanded in left-to-right order.

### Advantages and disadvantages of BFS

BFS is guaranteed to completely explore the search space, so if a path exists to the goal state, the method will find it.

The main advantage of BFS is that it always finds the solution that is the *minimum number of steps from the starting state*. This is, it will find the solution in the search tree that occurs at the shallowest possible level. This is good if you desire a solution that requires the minimum number of state changes to reach the goal.

The disadvantage of BFS is that the number of nodes in the frontier may grow exponentially. Let the branching factor of the search be *b*; that is, suppose that each node we expand creates *b* new children in the search tree. In that case,

- The root is 1 node
- The first level has *b* nodes
- The second level has *b*<sup>2</sup> nodes
- The third level has *b*<sup>3</sup> nodes

If the first solution occurs on level *k*, then the total number of nodes processed is on the order of

1 + *b* + *b*<sup>2</sup> + *b*<sup>3</sup> nodes + ... *b*<sup>*k*</sup>

which is *O*(*b*<sup>*k*</sup>).


