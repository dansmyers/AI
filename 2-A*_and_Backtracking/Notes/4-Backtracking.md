# Backtracking search

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg/1280px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png" width="300px" />

*Example Sudoku puzzle*, [Wikipedia](https://en.wikipedia.org/wiki/Sudoku)

## Constraint satisfaction problems

You're probably familiar with Sudoku puzzles like the one above. The goal is to place the digits 1-9 on the grid, such that each digit occurs exactly once in each row, once in each column, and once in the marked 3x3 subsquare. Sudoku is an example of a **constraint satistfaction problem** (CSP). A CSP is defined by three things:

- A set of *decision variables*. In Sudoku, each square can be thought of as a variable that's waiting to be assigned a number.

- A set of *values* that can be assigned to the variables. In Sudoku, these are the digits 1-9. This problem has only one value set that applies to all of the decision variables, but it's possible to come up with problems that have multiple sets of values, each for a different subset of the variables.

- The *constraints* that determine which assignments of values to variables are **valid**.

The overall goal of the problem is to find an assignment of variables to values that respects the constraints. We've already seen one example of a CSP, the *n*-queens problem:

- The decision variables are the column positions of the *n* queens, one per each row of the board
- The values are the column numbers 1 to *n*
- The constraints are the rules preventing queens from attacking each other

Note that a CSP is different from a planning problem, like the lights out puzzle or the eight puzzle, because the goal is only to verify if a solution *exists or doesn't exist*. There isn't a "path" or sequence of steps that we need to identify leading to the solution - a Sudoku puzzle is solved by showing the valid configuration of digits, not by specifiying some order of placing them in the puzzle.


## Backtracking search

Backtracking is the recursive implementation of depth-first search. It uses the recursive stack of function calls to keep track of the history of visited states rather than an explicit queue. Backtracking search is the preferred technique for solving CSPs.

Backtracking uses the strategy of trying to build a solution by assigning one variable at a time. If the method gets stuck, such that no more valid assignments are possible, it backtracks to the last previous step and tries a different choice. This approach will test each possible configuration of variables and values at most one time. It immediately abandons infeasible paths as soon as they're discovered, so you never waste time checking paths that can't possible lead to a satisfying solution.

The basic approach is as follows:

1. Choose an unassigned variable *v*. If all variables have been assigned, we're at a satisfying solution and the problem is solved.

2. Determine the set of values that can be assigned to *v* without violating the constraints. Choose one, assign it, then recursively continue the search.

3. If no valid values exist, then the search has reached a dead end. Backtrack to the previous decision and try a different assignment.

Here's the pseudocode implementation:
```
Backtracking search

input:
    valid function  // tests if an assignment is valid in current state

output:
    solution state if one is found, failure otherwise

search(state) {

  v = choose the next unassigned variable

  // All variables assigned: this is a solution
  if (v == null) {
    output current state as a solution and exit
  }

  // Recursively explore all valid assignments to v
  for each value s {

    // Test if assigment s is allowed for v in the current state
    if valid(s, v, state) {
      state[v] = s
      search(state)
    }
  }

  // There was no solution on this path
  //
  // Reset v, then backtrack to the previous decision
  state[v] = null
}
```

