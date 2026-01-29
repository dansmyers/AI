# Constraint Propagation

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg/1280px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png" width="300px" />

*Example Sudoku puzzle*, [Wikipedia](https://en.wikipedia.org/wiki/Sudoku)

## Overview

This note is short. After you read the basic concepts below, work through Peter Norvig's classic article, ["Solving Every Sudoku Puzzle"](https://norvig.com/sudoku.html), which will show you how to implement the actual Sudoku solver using the optimization techniques described below.


## The order of variables

Suppose you want to solve the Sudoku puzzle above using backtracking. The reasonable approach would be to start in the top row and work your way left to right, trying every possible number that can fit in each square.

- Start with the third square on the first row. Assign a 1 to that position.
- Then move to the fourth square. You can't place a 1, but you can place a 2.
- Move to the next open square on the first row. You can't place 1 or 2 (you used those already on the first row), or a 3 (it's in the column), but you could place a 4.

You can keep going with this approach. You'll eventually get stuck and have to backtrack, but this approach will eventually find valid assignments to every square.

However, look at the center square of the puzzle. It only has *one possible value*: 5. Once you assign that square, you don't ever need to consider it again for the rest of the search. You can find other squares that have only a few possible options. For example, the first square on row 3 can only be 1 or 2. 

The total number of possible states is multiplicative. In general, if there are *V* variables with *S* possible values, then the total number of states is *V*<sup>*S*</sup>. However, if one variable has only two possible states, then assigning one of its two options reduces the search space by ***50%***.

This is the first way to improve backtracking: when you choose the next variable to assign, choose *the most constrained variable*. Making a few choices on highly constrained variables can quickly reduce the effective size of the search space.

## Constraint propagation

If you assign 5 to the center square, it can't be used again in the center row, column, or 3x3 subsquare. Therefore, we can immediately remove 5 as an option for any of those squares.

The *constraint propagation* technique maintains a set of valid values for each variable - call this the *domain* of the variable. Whenever you assign a value to a variable during the search, use the constraints to eliminate inconsistent values from the domains of other unassigned variables. Ideally, this will allow you quickly identify the most constrained variables and aggressively shrink the search space.
