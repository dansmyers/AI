"""
N-Queens solution using breadth-first search
"""

from copy import copy

# The frontier of queue of solutions waiting to be explored
queue = []

N = 5

def print_solution(s):
  """
  Print the solution as a grid
  """
  print('')

  for row in range(N):
    for col in range(N):
      if col == s[row]:
        print('Q', end=' ')
      else:
        print('.', end=' ')
    print('')
    
  print('')


def is_valid(s):
  """
  Check if a given queen configuration is valid
  """
  
  first_row = 0
  while first_row < N and s[first_row] != -1:
    
    second_row = first_row + 1
    while second_row < N and s[second_row] != -1:

      # No two queens may be in the same column
      if s[first_row] == s[second_row]:
        return False

      # No two queens may be in the same diagonal
      row_dist = second_row - first_row
      col_dist = abs(s[second_row] - s[first_row])
      if row_dist == col_dist:
        return False

      second_row += 1
    first_row += 1

  # All tests pass
  return True


def queens():
  """
  Solve the N-Queens problem by breadth-first search
  """

  # Initialize starting state
  state = [-1 for i in range(N)]
  queue.append(state)

  while len(queue) > 0:
    # Pop the next search state
    state = queue.pop(0)

     # Find first -1 --> next empty position
    next_open_row = state.index(-1)

    # Generate possible successors
    for col in range(N):
      new_state = copy(state)
      new_state[next_open_row] = col

      if is_valid(new_state):
        if -1 not in new_state:
          print_solution(new_state)
        else:
          queue.append(new_state)

if __name__ == "__main__":
  queens()
