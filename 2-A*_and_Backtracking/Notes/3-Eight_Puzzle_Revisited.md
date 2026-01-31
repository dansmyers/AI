# Eight Puzzle with A* Search

## Overview

We looked at the eight puzzle in the last unit - slide the tiles to put them into the correct order. That version of the problem used iterative deepening. Let's update it to use A* search.

The main challenge of using A* search is coming up with a reasonable heuristic. Recall that the heuristic is usually created by *relaxing* constraints on the problem to come up with an easier problem that gives a lower bound on the real solution cost.

Consider this starting situation in the eight puzzle:
```
    8 |   | 6
    ---------
    5 | 4 | 7
    ---------
    2 | 3 | 1
```
Here's an option: Count the number of tiles that are in wrong positions. This is like allowing yourself to move any tile immediately to its correct position without worrying about conflicts - how many moves would that take? That's clearly nonnegative and a lower bound on the real number of moves, since any out of place tile has to move at least one position, so it's an admissible heuristic.


## Solution
This solution modifies the earlier iterative deepening version to use A* with the misplaced tiles heuristic. Notice how it uses a priority queue (via `heapq`) to maintain the frontier set. The key method is `misplaced_tiles`, which counts the number of tiles out of position:
```
def misplaced_tiles(state, goal):
    """
    Heuristic function: counts the number of tiles that are not in their goal position.
    The blank tile (0) is not counted as a misplaced tile.
    
    Args:
        state: Current state (tuple of 9 integers)
        goal: Goal state (tuple of 9 integers)
    
    Returns:
        Number of misplaced tiles (excluding the blank)
    """
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count
```
There's another optimization involving the `g_values` set. It keeps track of the best cumulative path cost known for each state. This is useful, because there may be multiple ways to get to a particular state, and we only need to use the lowest one. When a successor state is generated, we avoid reinserting known states into the frontier unless we've found a better path with a lower cumulative path cost.

```
"""
Eight Puzzle Solver using A* Search with Misplaced Tiles Heuristic

The 8-puzzle is represented as a tuple of 9 elements (0-8), where 0 represents
the blank tile. Index positions correspond to:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
"""

import heapq


def get_successors(state):
    """
    Generate all valid successor states from the current state.
    Returns a list of states reachable by sliding one tile into the blank.
    """
    successors = []
    state = list(state)
    blank_idx = state.index(0)
    
    # Define possible moves based on blank position
    # Maps each position to the positions it can swap with
    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }
    
    for swap_idx in moves[blank_idx]:
        new_state = state.copy()
        new_state[blank_idx], new_state[swap_idx] = new_state[swap_idx], new_state[blank_idx]
        successors.append(tuple(new_state))
    
    return successors


def misplaced_tiles(state, goal):
    """
    Heuristic function: counts the number of tiles that are not in their goal position.
    The blank tile (0) is not counted as a misplaced tile.
    
    Args:
        state: Current state (tuple of 9 integers)
        goal: Goal state (tuple of 9 integers)
    
    Returns:
        Number of misplaced tiles (excluding the blank)
    """
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def reconstruct_path(goal, parent):
    """
    Reconstruct the path from initial state to goal by following parent pointers.
    """
    path = []
    current = goal
    
    while current is not None:
        path.append(current)
        current = parent[current]
    
    path.reverse()
    return path


def a_star_search(initial, goal):
    """
    A* Search with misplaced tiles heuristic.
    
    A* uses f(n) = g(n) + h(n) where:
        - g(n) = cost to reach node n from start (number of moves)
        - h(n) = heuristic estimate (misplaced tiles count)
    
    Args:
        initial: Starting state (tuple of 9 integers)
        goal: Goal state (tuple of 9 integers)
    
    Returns:
        List of states from initial to goal if solution exists, None otherwise
    """
    if initial == goal:
        return [initial]
    
    # Priority queue: (f_value, counter, g_value, state)
    # Counter is used to break ties and ensure FIFO ordering for equal f-values
    counter = 0
    h_initial = misplaced_tiles(initial, goal)
    frontier = [(h_initial, counter, 0, initial)]
    
    # Track the best g-value found for each state
    g_values = {initial: 0}
    
    # Parent pointers for path reconstruction
    parent = {initial: None}
    
    # Set of fully expanded states
    closed = set()
    
    while frontier:
        f, _, g, state = heapq.heappop(frontier)
        
        # Skip if we've already expanded this state
        if state in closed:
            continue
        
        # Check for goal
        if state == goal:
            return reconstruct_path(state, parent)
        
        # Mark as expanded
        closed.add(state)
        
        # Expand successors
        for successor in get_successors(state):
            new_g = g + 1  # Each move costs 1
            
            # Skip if already expanded with a better or equal path
            if successor in closed:
                continue
            
            # Only process if this is a new state or we found a better path
            if successor not in g_values or new_g < g_values[successor]:
                g_values[successor] = new_g
                parent[successor] = state
                h = misplaced_tiles(successor, goal)
                f = new_g + h
                counter += 1
                heapq.heappush(frontier, (f, counter, new_g, successor))
    
    # No solution found
    return None


def print_state(state):
    """Pretty print a puzzle state."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else ' ' for x in state[i:i+3]]
        print(' | '.join(row))
        if i < 6:
            print('---------')


def print_solution(path):
    """Print the solution path with step numbers."""
    if path is None:
        print("No solution found.")
        return
    
    print(f"Solution found in {len(path) - 1} moves:\n")
    for i, state in enumerate(path):
        print(f"Step {i}:")
        print_state(state)
        print()


if __name__ == "__main__":
    goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    initial = (8, 0, 6, 5, 4, 7, 2, 3, 1)
    
    path = a_star_search(initial, goal)
    print_solution(path)
```

## A stronger heuristic

Think about the puzzle. Is there a better heuristic that counting out-of-place tiles?

Yes, it turns out that our previous friend the Manhattan distance also works for this problem. To move a tile into its correct position, it must, at minimum, move the combined horizontal and vertical distances to its correct location.

The Manhattan distance is better than misplaced tiles, because it's a *tighter lower bound*. That is, it's still a lower bound, but one that's closer to the real number of moves needed to reach the true solution. That means the Manhattan distance will allow us to more aggressively prune paths from the search. Intuitively, using a stronger admissible heuristic can only make the search better, never worse. 

The Manhattan distance heuristic for the eight puzzle is the sum of the Manhattan distances for each individual tile. Take a look at the implementation below. Observe how it calculuates the row and column position of the current and goal positions, then uses the Manhattan distance formula.
```
def manhattan_distance(state, goal):
    """
    Heuristic function: sum of Manhattan distances for all tiles.
    For each tile, calculates the horizontal and vertical distance
    from its current position to its goal position.
    The blank tile (0) is not counted.
    
    Args:
        state: Current state (tuple of 9 integers)
        goal: Goal state (tuple of 9 integers)
    
    Returns:
        Sum of Manhattan distances for all tiles
    """
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            goal_idx = goal.index(tile)
            current_row, current_col = i // 3, i % 3
            goal_row, goal_col = goal_idx // 3, goal_idx % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance
```
