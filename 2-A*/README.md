# A* Search

## Due Wednesday, February 28

## You can work with a partner on this project

## Overview

The problems in this assignment will let you practice using dynamic programming and A* search. They're pretty straightforward. Submit your solutions on Canvas.

The second phase of the paper project is the literature review, described in `Paper.md`. Complete the tasks described there and then upload your work in a file to the assignment on Canvas that I'll create.

## Dynamic programming practice

<img src="https://i.pinimg.com/originals/5c/2e/7b/5c2e7b63caf86c3a9a77abd4da2ead0d.jpg" width="30%" />

### 0/1 knapsack

Write a program that implements the matrix-based solution to the 0/1 knapsack problem. Use the file `knapsack.py`, which contains code to automatically generate some randomized values and weights.

- Start by in initializing the first row and first column of the matrix with zeros to represent the base cases.

- Then use the recursive formulation we derived in class to calculate the value for each matrix entry in terms of previously-completed entries. Remember that you also need to check if there is spare capacity for an item; if it doesn't fit, you can't add it.

- Print your matrix at the end of the program. The solution is in the lower-rightmost position.

To be clear: Don't implement the recursive solution to the problem. You must use the table-based solution with *no recursive function calls*.

### 0/1/2 knapsack

Now modify the program to solve the **0/1/2 knapsack problem**, where you can take either 0, 1, or ***2*** copies of an item.

To design a solution, use the same strategy as before. Consider the last item *n*. There are three options:

1. Skip item *n*, and find the optimal solution of the first *n* - 1 items

2. Take one copy of item *n*. This is the same as taking the item in the 0/1 version of the problem.

3. Take *two copies* of item *n*. In this case, you gain a value of 2*v*<sub>*n*</sub> but also pay a weight of 2*w*<sub>*n*</sub>.

Modify the algorithm to incorporate the option of taking two of each item. Again, use the table-based solution approach and print your table at the end of the problem.

Put your solution in a file named `knapsack2.py`.


## Motion planning

Consider a robot planning a path through a grid-based world. Its goal is to move from a start square in the upper-left to a goal square in the lower-right, moving around any obstacles in its way.

Let's make some assumptions:
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

Write a program that uses A* search to find the shortest path from the start to the goal in a randomly generated grid world, or discover that no
path exists. Use the *Manhattan distance* from the current position to the goal square as your heuristic.

Use the `motion.py` script as a starting point, which includes code to randomly generate ten trial worlds. Your program should print out the solution grid, showing the shortest path in stars, as in the example above, or a message that no path exists if the search fails.


Tips:

- Review the eight puzzle solution posted in the Examples directory

- A* is based on a breadth-first search, so it should use the same basic structure as our other breadth-first search problems

- To insert items into the priority queue, package them as tuples: `queue.put((priority, state))`
  
- When you get the smallest item from the queue, it will be returned as a tuple, the same way it was inserted:
```
queue_entry = queue.get()
state = queue_entry[1]
```

- A* also requires you to keep track of each solution's distance from the start space. \emph{This is not the same as the Manhattan distance
to the start space}! Each State object must have a variable that tracks how many moves have been taken to reach it.
