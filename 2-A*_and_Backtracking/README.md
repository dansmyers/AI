# Sprint 2: A*, Constraint Satisfaction, and Backtracking

## Overview

This unit continues our investigation of search algorithms. The last sprint looked at BFS and DFS and some important variations. These methods could solve problems optimally, but they were not always efficent.

We're going to look at two more strategies:

- **A\***, which uses a heuristic function to estimate the distance to the goal and guide the search in productive directions. A* is guaranteed to find an optimal solution if one exists and to do so efficiently.

- **Backtracking search**, which is used to solve **constraint satisfaction problems**. Backtracking is essentally a recursive formulation of depth-first search.

- We'll also look at one particular CSP: **boolean satisfiability**, which is one of the most important problems in theoretical computer science.

## Topics

- Heuristic functions
- Greedy best-first search
- A* search
- Admissible heuristics
- Proof of the optimality of A*
- Constraint satisfaction problems
- Backtracking for CSPs
- Constraint propagation
- Boolean satisfiability and 3-CNF-SAT

## Deliverables

Complete the three projects in the `Deliverables` directory. Use Claude Code to help you with each one. One of the keys of this unit is to practice *developing incrementally*. Pay attention to the advice on building the projects in steps and testing as you go!

If you haven't done so, move your Sprint 1 project into its own directory. Create new directory to hold the specs, code, etc. for each project in this unit; don't try to keep everything in one big directory with no organization.

## Resources

- Start with the notes in the `Notes` directory

- Look at section 1.4 of the [Berkeley text](https://inst.eecs.berkeley.edu/~cs188/textbook/search/informed.html). Pay attention to the proof of the optimality of A* using admissible heuristics. You don't need to read section 1.5 on local search yet.

- Chapter 2 covers constraint satisfaction problems. Look at sections 2.1 and 2.2. You can skim 2.3 and 2.4: they both discuss strategies for optimizing the basic backtracking solution algorithm. The core concepts (filtering and ordering) are pretty easy to understand. We're not going to discuss the specific methods they describe (arc consistency and tree structure).

- [This is another nice overview of A*](https://www.redblobgames.com/pathfinding/a-star/introduction.html). It uses a similar motivating example as the first note.

- If you want to read more about NP-completeness (not required for this sprint, but an important application of satisfiability), check out my old [COVID-era notes](https://github.com/dansmyers/Algorithms/blob/master/Challenge_Projects/2-The_Lost_Sprint.md) from the Algorithm Analysis class.
