"""
Generate Latin Squares using backtracking
"""

def print_square(square):
  print('')
  for i in range(N):
    print(square[i])
  print('')


def find_unassigned(square):
  for i in range(N):
    for j in range(N):
      if square[i][j] == 0:
        return i, j

  return -1, -1


def is_valid(square, r, c, value):
  for i in range(N):
    if square[r][i] == value or square[i][c] == value:
      return False

  return True


def solve(square):

  # Find the next unassigned variable
  r, c = find_unassigned(square)
        
  # If there is no unassigned variable, solution
  # has been found
  if r == -1 and c == -1:
    print_square(square)
    exit(0)

  # Consider its possible assignments
  for value in range(1, N + 1):

    # If the possible solution is valid, explore
    # from that point forward
    if is_valid(square, r, c, value):
      square[r][c] = value
      solve(square)

  # If we reach here, we never found a solution,
  # clear the assignment and backtrack
  square[r][c] = 0


### Main
N = 5

square = [[0 for i in range(N)] for i in range(N)]
print_square(square)

solve(square)
