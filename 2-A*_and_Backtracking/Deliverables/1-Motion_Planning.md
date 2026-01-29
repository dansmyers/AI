# Motion Planning with A*


## Overview
Let's return to the example of the robot planning a path through a grid-based world. Its goal is to move from a start square in the upper-left to a goal square in the lower-right, moving around any obstacles in its way.

Your goal in this project is to implement a motion planning program that uses A* search and works on randomized grid worlds. Your goal is to find the shortest path from the start to the goal in a randomly generated grid world, or discover that no path exists.

Use the **Manhattan distance** from the current position to the goal square as your heuristic.

Use the `motion.py` script in this directory as a starting point, which includes code to randomly generate ten trial worlds. Your program should print out the solution grid, showing the shortest path in stars, as in the example above, or a message that no path exists if the search fails.

## World description

- The world is a *R* by *C* grid, indexed from 0 in both dimensions

- The start square is always at position (1,1)

- The goal square is always at position (*R* - 2, *C* - 2)

- Obstacles in the grid have the value 1 and free squares have the value 0.

- The boundaries of the world are always enclosed by walls of 1's, so we don't need to consider special cases
for stepping off the edge of the grid.

- The robot can move up, down, left, and right, but not diagonally.

Here's an example 10x30 grid world. The shortest path is marked in stars. For clarity, the zeros have been replaced by spaces.
```
111111111111111111111111111111
1**********           1      1
1    11111*           1      1
11111   ***           11111111
1       *111111111111111     1
1       *****                1
1     111111*                1
1           *                1
1           *****************1
111111111111111111111111111111
```

## Claude Code's plan mode

Use Claude Code to help you. I recommend making a new directory to hold this project:
```
mkdir 2-Motion_Planning
```
Start by putting `motion.py` in that directory.

Run `claude`, then enter **planning mode** by typing `/plan` at the prompt. Planning mode lets you chat about the existing code and problem in read-only mode. Claude can make suggestions, prompt for details, and so forth, but without kicking off any actions that will modify or create files.

Work in planning mode to develop your approach. Once you have a good plan, you can then exit plan mode and have Claude perform the implementation.

### Plan mode vs. specs documents
Planning is a complement to building the formal specs document like we did in the last project.

- For small features in an existing code base, planning is probably sufficient

- For establishing the initial design of a new application, use a formal specs document. If the set of required features for the application changes in a fundamental way, update the specs to reflect the change. In general, think of the specs document as the "ground truth" for what the application is and is supposed to do.


## Other tips

- Review the eight puzzle solution
- A* is based on a breadth-first search, so it should use the same basic structure as our other breadth-first search problems
- To insert items into the priority queue, package them as tuples: `queue.put((priority, state))`
- When you get the smallest item from the queue, it will be returned as a tuple, the same way it was inserted:
