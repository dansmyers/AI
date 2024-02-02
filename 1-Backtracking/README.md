# Assignment 1: Backtracking Search

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

<img src="https://upload.wikimedia.org/wikipedia/commons/0/00/Futoshiki1.png" width="33%" />

Write a solver for the Futoshiki puzzles described at the end of the book chapter. Again, think about using the backtracking search strategy with custom methods that implement the variable selection and constraints.

- Again: does the overall solution strategy change? No! Keep the same backtracking search framework as the Latin square and Sudoku examples.

- Put your solution in a file named `futoshiki.py`.

- Use the example puzzle in the chapter as a test and verify that you can solve it correctly.


### Lights Out

Another classic puzzle. You're given a N x N grid of button lights, all of which are initially *ON*. Pressing a button toggles the state of its four neighbors in the up, down, left and right directions.

<img src="https://miro.medium.com/v2/resize:fit:1185/1*Ee91-MD7MSjG5X9lvlOiqA.png" width="50%" />

*Example by K.L. deVries on [Medium](https://medium.com/swlh/programming-puzzle-lights-toggle-f4d27bf3683e)*

Your goal is to find the combination of button presses that turns all the lights *OFF*. Write a program that uses **backtracking with iterative deepening** to find the solution.

- Modify the basic recursive backtracking search to take additional `current_depth` and `max_depth` parameters. If the `current_depth` exceeds the `max_depth`, treat it as a base case and return immediately.

- For a given state, there are *N*<sup>2</sup> possible moves to consider, which correspond to each possible button press.

Consider why iterative deepening is a good strategy for this problem. You're allowed to press each button as many times as you want, so there's no limit on the depth of any path. Left unchecked, you would simply descend the search tree, pressing buttons to create an infinitely long path that might never lead to a solution. Iterative deepening ensures that you consider all button combinations up to a certain depth before exploring deeper paths.

A pseudocode version of the `solve` method is as follows:

```
def solve(lights, current_depth, max_depth):
  """
  Recursive backtracking solution to the lights out puzzle
  """

  # Depth limit reached
  if current_depth > max_depth:
    return

  # Determine if the current state is a solution
  if all_lights_are_off(lights):
    print(presses)  # Print the sequence of button presses that led to the solution
    exit(0)

  # Consider all of the N * N button presses
  for row in range(N):
    for col in range(N):
      # Determine the state of pressing button at position (row, col)
      lights = flip(lights, row, col)

      # Keep track of the sequence of button presses
      presses.append((row, col))

      # Recursively search
      solve(lights, current_depth + 1, max_depth)

      # Undo the effect of flipping (row, col) to prepare for the next option
      lights = flip(lights, row, col)
      presses.pop()

  # If you get here, there was no solution on this path: backtrack
```

You'll need to figure out how to implement the relevant methods (`all_lights_are_off` and `flip`), then write an outer function that runs the search for increasing values of `max_depth` until it finds a solution.

The pseudocode assumes that you're keeping track of the state of the lights using an *N* by *N* list of lists, which is fine. The variables `presses` is a list that keeps track of the sequence of button presses used to find the solution.

Start with a small grid, say 3 x 3, then try solving for larger grids.
