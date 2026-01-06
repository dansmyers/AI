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

BFS is guaranteed to completely explore the search space, so if a path exists to the goal state the method will find it.

The main advantage of BFS is that it always finds the solution that is the *minimum number of steps from the starting state*. That is, it will find the solution in the search tree that occurs at the shallowest possible level. This is good if you desire a solution that requires the minimum number of actions to reach the goal.

The disadvantage of BFS is that the number of nodes in the frontier may grow exponentially. Let the branching factor of the search be *b*: each node we expand creates *b* new children in the search tree. In that case,

- The root is 1 node
- The first level has *b* nodes
- The second level has *b*<sup>2</sup> nodes
- The third level has *b*<sup>3</sup> nodes

The total number of nodes processed is on the order of

1 + *b* + *b*<sup>2</sup> + *b*<sup>3</sup> nodes + ... *b*<sup>*k*</sup>

which is *O*(*b*<sup>*k*</sup>). (See section 1.3 of the Berkeley text).

The space complexity is even worse. Finding the solution on level *k* requires processing nodes on that level, which generates the nodes on level *k* + 1. Therefore, the frontier has to hold *O*(*b*<sup>*k* + 1</sup>) nodes.

Therefore, if the search tree truly grows exponentially,  we shouldn't expect to find a solution from basic breadth-first search for anything other than small problems. BFS can still be viable in practice if most states generate only a few successors.


## Depth-first search

DFS uses a **last-in-first-out stack** as its data structure. This corresponds to expanding the **deepest** node in the search tree. In effect, DFS chooses one path and explores it to completion, then moves to the next-deepest known path, and so forth.

In our Florida example, we'd start by expanding Tallahassee, as before. The frontier stack looks like the following:
```
 Jacksonville
   Pensacola
  Gainesville
---------------
```
The next step chooses the top of the stack, Jacksonville in this case, and pushes its successors on top:
```
     Tampa
    Orlando
   Pensacola
  Gainesville
---------------
```
The next step will expand Tampa, which will lead to finding the path to Naples and then Miami.

Life BFS, the depth-first strategy doesn't consider cost or try to choose "good" nodes, so it's not guaranteed to return the minimum-cost solution. It's also not guaranteed to find the shallowest solution, since it doesn't process nodes in level order.

The main advantage of DFS is that it only needs to store the current path, plus unexpanded siblings of nodes on the path. This is almost always much more manageable than the full levels generated by BFS. For problems like our Florida map, where most choices either result in dead ends or make progress toward the goal, DFS will quickly find a viable path and tear its way down to the solution.

However, the basic DFS has no way to stop exploring its current path as long as it can continue to generate new nodes. The risk of depth-first search is getting stuck on a very deep path that never leads to a solution. The **iterative deepening** method that we'll examine in a future note addresses this problem.


## "Uninformed search"

BFS and DFS always choose the next node in their respectivve data structures to expand. These methods are called "uninformed" in the sense that the sequence of expansions is determined by the order the nodes are inserted and not any property of the nodes themselves. A better solution might try to choose "good" nodes (for some definition of good) so that we can make progress towards the solution without expanding too many unnecessary nodes. The next unit will look at these "informed" search techniques, the most important of which is the **A\* search** algorithm.

The next note will show you how to actually implement BFS and DFS for a real problem, then we'll consider two more uninformed methods: iterative deepening and uniform cost search.









