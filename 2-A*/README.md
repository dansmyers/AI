# A* Search

## Due

## You can work with a partner on this project

## Overview



## Dynamic programming practice

<img src="https://i.pinimg.com/originals/5c/2e/7b/5c2e7b63caf86c3a9a77abd4da2ead0d.jpg" width="35%" />

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

