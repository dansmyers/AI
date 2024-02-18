"""
Knapsack problem
"""

import random


def knapsack(values, weights, max_capacity):
  """
  Solve 0/1 knapsack using the given parameters

  Complete the method to use the table-based solution
  """


### Main
if __name__ == '__main__':
  N = 15
  
  values = [random.randint(1, 10) for i in range(N)]
  weights = [random.randint(1, 10) for i in range(N)]

  print('values = ' + str(values))
  print('weights = ' + str(weights))

  capacity = 25

  knapsack(values, weights, capacity)
