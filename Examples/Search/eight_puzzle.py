# The 8-Puzzle using A* search
# DSM, 2017

from queue import PriorityQueue  # For priority queues
from copy import deepcopy


class State(object):

    def __init__(self, puzzle, path):
        self.puzzle = puzzle
        self.path = path


    def hamming_distance(self):
        """
        Calculate hamming distance to the solution, which is the number of
        tiles that are out of their correct position
        """

        distance = 0

        for i in range(9):

            # Calculate the correct row and column for value i
            row = i // 3
            col = i % 3

            # If value is not in the correct position, add 1 to the distance
            if self.puzzle[row][col] != i:
                distance += 1

        return distance


    def move(self, direction):

        # Find the index of the blank space
        for row in range(3):
            for col in range(3):
                if self.puzzle[row][col] == 0:
                    blank_row = row
                    blank_col = col

        swap_row = blank_row
        swap_col = blank_col

        # Check if the move is compatible with the blank position
        if direction == 'up' and blank_row != 0:
            swap_row = blank_row - 1
            swap_col = blank_col

        if direction == 'down' and blank_row != 2:
            swap_row = blank_row + 1
            swap_col = blank_col

        if direction == 'left' and blank_col != 0:
            swap_row = blank_row
            swap_col = blank_col - 1

        if direction == 'right' and blank_col != 2:
            swap_row = blank_row
            swap_col = blank_col + 1

        # Generate a new state from the swap if it's possible
        if swap_row != blank_row or swap_col != blank_col:
            new_puzzle = deepcopy(self.puzzle)
            temp = new_puzzle[blank_row][blank_col]
            new_puzzle[blank_row][blank_col] = new_puzzle[swap_row][swap_col]
            new_puzzle[swap_row][swap_col] = temp

            new_path = deepcopy(self.path)
            new_path.append(direction)

            return State(new_puzzle, new_path)

        # If the swap was not possible, return None
        else:
            return None


    def finished(self):
        for i in range(9):
            row = i // 3
            col = i % 3
            if self.puzzle[row][col] != i:
                return False

        return True


    def reconstruct_path(self):
        puzzle = [[7, 2, 4],
                  [5, 0, 6],
                  [8, 3, 1]]

        state = State(puzzle, [])

        for move in self.path:

            state = state.move(move)

            for row in range(3):
                for col in range(3):
                    print(str(state.puzzle[row][col]) + ' ',end='')
                print('')
            print('')


    def __lt__(self, other):
      """
      Define a < operator for comparing states to each other
      """
      return self.hamming_distance() < other.hamming_distance()


def previously_visited(s, visited):

    # Convert the puzzle board of state s from a list of lists to a tuple of
    # tuples -- recall that tuples can be dictionary keys
    key = (tuple(s.puzzle[0]), tuple(s.puzzle[1]), tuple(s.puzzle[2]))

    if key in visited:
        return True
    else:
        visited[key] = True
        return False


def solve():

    # Create a priority queue
    queue = PriorityQueue();

    # Set up the initial state
    # Let 0 represent the position of the blank
    puzzle = [[7, 2, 4],
              [5, 0, 6],
              [8, 3, 1]]

    initial_state = State(puzzle, [])


    # Insert the state as a (priority, data) tuple
    queue.put(initial_state)

    # Dictionary of previously visited states
    visited = {}

    # Loop until a solution is achieved or all states have been evaluated
    while queue.qsize() > 0:

        # Pop the state with the smallest f-value
        state = queue.get()

        # If this state is a solution, declare victory and exit
        if state.finished():
            print(state.puzzle)
            print(state.path)
            state.reconstruct_path()
            return

        for direction in ['up', 'down', 'left', 'right']:

            # Try to move the blank tile in the specified direction
            # State.move returns None if the move is impossible
            new_state = state.move(direction)
            if new_state is None:
                continue

            # If the state has not been visited, add it to the queue
            if not previously_visited(new_state, visited):

                # Insert into the priority queue
                queue.put(new_state)


if __name__ == '__main__':
    solve()
