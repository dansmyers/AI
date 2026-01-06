# Breadth-First and Depth-First Search

## Overview

The previous note discussed the basic strategy of state-space search for solving planning problems: given an initial state, explore the search tree until you find a sequence of actions leading to the goal state. We were vague, though, on how to practically implement this strategy for a real problem.

We're going to look at the two canonical search algorithms: breadth-first and depth-first search (BFS and DFS), which are really almost the same method. These are standard techniques that show up again and again throughout computer science in a variety of different contexts, including path finding in networks, graph analysis, and game playing. By themselves, BFS and DFS may not be suitable for every problem, but they're still the building blocks of more advanced techniques.

Make sure you've reviewed the previous material, particularly the pseudocode for tree search before continuing with this note.

## Breadth-first search

Recall that the tree search method uses a data structure called `frontier` to maintain the set of known but still unexpanded search tree nodes. The breadth-first search algorithm uses a **first-in-first-out queue** as the frontier structure. At each step, it chooses the *oldest* known node (that is, the node that was identified earliest in the search process) and expands it.

Consider the following abstract map of some major cities in Florida. The edges represent approximate routes.

<img src="../Images/florida_cities.png" width="400px" />

*Made with Claude Opus 4.5. Everything is approximate. This is inspired by a similar example in Russell and Norvig's Artificial Intelligence: A Modern Approach that used a map of cities in Romania.*



