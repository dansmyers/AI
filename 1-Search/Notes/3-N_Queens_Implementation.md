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

To expand a node, identify the next open row and place queens any columns that don't conflict with the queens that are already on the board. The first step generates the successors of the initial state by placing one queen in each column of the first row. The figure below shows the search tree for the 4-queens problem. Observe that the first step generates four children, one for each column in the first row, but the subsequent expansions quickly run out of viable positions to place queens.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdxZspJTMWXqrhauYV8E-GK4Qjzf_YA6zNWA&s" width="400px" />

