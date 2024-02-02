# Assignment 1: Solving Problems by Searching

## Due

## You can work with a partner to complete this assignment

## Overview


## Problems

### Sudoku

For a warm-up, modify the Latin square solver given in the Examples directory to solve Sudoku puzzles. A Sudoku solution is a 9 x 9 Latin square where each digit 1 to 9 is also constrained to appear exactly once in each 3 x 3 subsquare.

- Think about what you need to change to add the initial constraints. Does the basic solution method change? No! All you really need to update is the `is_valid` method.

- Look at the relevant section in the book chapter, which has some tips on determining the 3 x 3 square.

- Put your program in a file named `sudoku.py`.

- Use the example Sudoku puzzle at the start of the book chapter as test data.


### Futoshiki

Write a solver for the Futoshiki puzzles described at the end of the book chapter. Again, think about using the backtracking search strategy with custom methods that implement the variable selection and constraints.

- Again: does the overall solution strategy change? No! Keep the same backtracking search framework as the Latin square and Sudoku examples.

- Put your solution in a file named `futoshiki.py`.

- Use the example puzzle in the chapter as a test and verify that you can solve it correctly.
