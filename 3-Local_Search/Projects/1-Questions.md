# Written Questions

## Overview

Complete the questions below. Write your answers legibly and turn in a scan or photo.

## Knapsack

###

### 0/1/2 

Derive a solution to the 0/1/2 problem, where you may take up to two of each item. Tips:

- There are three cases to consider: taking 0, taking 1, or taking 2
- The 0 and 1 cases are the same as the standard knapsack problem
- Think about how the total value and available capacity change in the 2 item case

### Subset sum

You’re given an array of integers (each of which might be positive or negative) and a target value T. Design a method to verify if a subset of the integers sums to exactly T.

For example, if the array is
```
[2, 3, 5, 7, 11, 13]
```
and the target is 20, the answer is True because 2 + 7 + 11 sums to 20. Note that more than one solution is allowed; 7 + 13 would also be a valid subset.

Tips:

Sometimes things that seem different are almost the same. This feels very similar to the 0-1 knapsack, but it’s a decision problem, not an optimization, so the result must be boolean True or False.

Suppose you’re considering the last item, the 13. There are three possibilities:

13 by itself is the target. You can return True immediately.

13 is not the target but is included in the sum. In this case, you need to check the other items to see if you can find a subset that adds to T - 13.

13 is not included in the sum. In this case, check the other items for a sum of T.

Use these ideas to write down the recursive relationship and base cases, then work out a bottom-up strategy for solving the problem.
