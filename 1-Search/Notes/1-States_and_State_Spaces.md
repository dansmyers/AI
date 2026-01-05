# States and State Spaces


## A river crossing problem

You've probably seen riddles that involve taking objects across a river, like the one about the farmer who needs to transport his chicken, grain, and fox. Here's another one that we'll use for our starting example.

> A group of three AI researchers and three robots needs to reach the other side of a river. Their boat can only carry at most two entities at a time (two humans, two robots, or one of each). Unfortunately, the ethical control units of the robots are still a bit misaligned, so the robots can never be allowed to outnumber the humans on either side of the river at any time.
>
> Formulate a plan to move everyone to the other side of the river without provoking a robot uprising.

This problem was considered in an important [early AI paper from 1968](https://courses.cs.umbc.edu/471/spring23/02/resources/MI3-Ch.10-Amarel.pdf) by Saul Amarel, as the (regrettably named) "missionaries and cannibals problem". Amarel's paper gave a formal way of defining planning problems that could be solved by search algorithms.

## States


