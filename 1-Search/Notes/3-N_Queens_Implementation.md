# The *N*-Queens Problem


<img src="https://yue-guo.com/wp-content/uploads/2019/02/N_queen.png" width="400px" />

*A solution to the 8-queens problem, from Yue Guo. Observe that no two queens lie in the same row, column, or diagonal.*


## Overview

The last note looked at breadth-first and depth-first searches in a general way. Our goal in this note is to show how to move from the high-level tree search pseudocode to a real implementation.

The ***n*-queens problem** is a classic planning puzzle that's frequently used an example for search problems. The queen piece in chess can move any number of squares horizontally, vertically, or diagonally. Given an *n*-by-*n* chessboard, can you place *n* queens such that no two queens can attack each other? The original version used a standard 8x8 chessboard with 8 queens, one solution of which is shown above.

Recall that the challenge of implementing a search algorithm isn't in *deciding* to use search: it's in working out the details, including:

- An efficient state representation
- A way of generating valid successor states
- Keeping track of visited states
- Recognizing when you've reached the goal state

## State representation

Let's start with a basic observation: there has to be exactly one queen per row. Therefore, we don't need to track the exact (row, column) position of each queen, we just need to track the columns assigned to the queens on row 0, row 1, and so forth.

The state will be represented by a tuple where each entry contains the column of one placed queen. The solution above has the representation `(4, 1, 3, 6, 2, 7, 5, 0)`.

## Generating successors

Begin with an empty board as the initial state. This corresponds to an empty state tuple, `()`, since no queens have been placed.

To expand a node, identify the next open row and place queens any columns that don't conflict with the queens that are already on the board. The first step generates the successors of the initial state by placing one queen in each column of the first row. The figure below shows the search tree for the 4-queens problem. 

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdxZspJTMWXqrhauYV8E-GK4Qjzf_YA6zNWA&s" width="400px" />

*[Panruo Wu](https://www2.cs.uh.edu/~panruowu/2023f_cosc3320/lec3_backtrack.pdf), University of New Hampshire*

Observe that the first step generates four children, one for each column in the first row, but the subsequent expansions quickly run out of viable positions to place queens.

From a state representation standpoint, the first levels of the tree look like the following:
```
                          ( )
                           |
        ---------------------------------------
       |              |         |              | 
      (0)            (1)       (2)            (3)
       |              |         |              |
   ---------          |         |          ---------
  |         |         |         |         |         |
(0, 2)    (0, 3)    (1, 3)    (2, 0)    (3, 0)    (3, 1)
```
Take a moment to compare the two trees and make sure that you understand how each tuple corresponds the given queen positions.

### Practice question

Construct the rest of the search tree for the 4-queens problem.

## Solution code

The program below is based on the tree search pseudocode from note #1. It uses a Python list as a FIFO queue to manage the states. Each state is represented as a tuple. The `get_successors` takes a current state as input and generates its successors by appending the valid column positions for the queen in the next row. The solution state is obtained when the state tuple has *n* entries.

The `is_safe` method is straightforward: it takes a state tuple, row, and column as inputs and checks if placing a queen at that (row, column) position would conflict with any already placed queens.

This version stops when it finds *the first solution*.  A variation is to keep going and return a list of all solution states for a particular size.

```
"""
N-queens problem using breadth-first search

DSM and Claude, 2026
"""

def is_safe(state: tuple, row: int, col: int) -> bool:
    """
    Check if placing a queen at (row, col) is safe given the current state.
    
    Args:
        state: Current partial solution (tuple of column positions)
        row: Row to place the new queen
        col: Column to place the new queen
    
    Returns:
        True if placement is safe, False otherwise
    """

    # The built-in enumerate function generates (index, value) pairs for the items
    # in the tuple
    for r, c in enumerate(state):

        # Check column conflict (row conflict is impossible by construction)
        if c == col:
            return False

        # Check diagonal conflict
        if abs(r - row) == abs(c - col):
            return False

    # No conflict was found, so this placement is valid
    return True


def get_successors(state: tuple, n: int) -> list:
    """
    Generate all valid successor states by placing a queen in the next row.
    """

    successors = []
    row = len(state)  # Next row to place a queen
    
    if row >= n:
        return successors
    
    for col in range(n):

        # If (row, col) is a safe position, create a successor by appending
        # col to the current state tuple
        if is_safe(state, row, col):
            successors.append(state + (col,))
    
    return successors


def is_goal(state: tuple, n: int) -> bool:
    return len(state) == n


def solve_n_queens_bfs(n: int) -> tuple:
    """
    Solve the N-Queens problem using Breadth-First Search.
    
    Args:
        n: Size of the board (number of queens)
    
    Returns:
        A tuple representing a valid solution, or None if no solution exists
    """
    if n <= 0:
        return None
    
    # Initialize empty frontier structure (queue for BFS)
    frontier = []
    
    # Begin with the starting state (empty board)
    initial_state = ()
    frontier.append(initial_state)

    while len(frontier) > 0:
        # Pop from the front of the queue
        x = frontier.pop(0)
        
        # If x is the goal state, we're done
        if is_goal(x, n):
            return x  # Output success
        
        # Generate successors of x
        s = get_successors(x, n)
        
        # Insert new unvisited successor states into frontier
        for i in s:
            frontier.append(i)
    
    # No solution was found
    return None


def print_board(solution: tuple) -> None:
    """
    Print the chessboard with queens placed.
    """
    if solution is None:
        print("No solution found")
        return
    
    n = len(solution)
    print(f"\n{n}-Queens Solution:")
    print("+" + "---+" * n)
    
    for row in range(n):
        line = "|"
        for col in range(n):
            if solution[row] == col:
                line += " Q |"
            else:
                line += "   |"
        print(line)
        print("+" + "---+" * n)


### Main
for n in range(1, 10):
    solution = solve_n_queens_bfs(8)
    print_board(solution)
```

## Practice

- Run the program and verify that it works. Make sure that you understand the interactions between the main loop, `get_successors`, and `is_safe`

- The solution doesn't keep the history of visited states, or check that a state is new before adding it to the frontier. Explain why that's okay.

- Experiment with increasing the size. How large can you make the problem before the solver seems to struggle?

- What would you need to change to make this a depth-first solver?





