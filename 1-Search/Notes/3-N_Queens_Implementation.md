# The *N*-Queens Problem


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Chessboard480.svg/500px-Chessboard480.svg.png" width="400px" />

*A solution to the 8-queens problem, from Wikipedia*


## Overview

The last note looked at breadth-first and depth-first searches in a general way. Our goal in this note is to show how to move from the high-level tree search pseudocode to a real implementation.

The ***n*-queens problem** is a classic planning puzzle that's frequently used an example for search problems. The queen piece in chess can move any number of squares horizontally, vertically, or diagonally. Given an *n*-by-*n* chessboard, can you place *n* queens such that no two queens can attack each other? The original version used a standard 8x8 chessboard with 8 queens, one solution of which is shown above.

Recall that the challenge of implementing a search algorithm isn't in *deciding* to use search: it's in working out the details, including:

- An efficient state representation
- A way of generating valid successor states
- Keeping track of visited states
- Recognizing when you've reached the goal state




