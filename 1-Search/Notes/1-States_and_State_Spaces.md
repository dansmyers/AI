# States and State Spaces


## River crossing problem

You've probably seen riddles that involve taking objects across a river, like the one about the farmer who needs to transport his chicken, grain, and fox. Here's another one that we'll use for our starting example.

> A group of three AI researchers and three robots needs to reach the other side of a river. Their boat can only carry at most two entities at a time (two humans, two robots, or one of each, or a single human/robot). Unfortunately, the ethical control units of the robots are still a bit misaligned, so the robots can never be allowed to outnumber the humans on either side of the river at any time.
>
> Formulate a plan to move everyone to the other side of the river without provoking a robot uprising.

This problem was considered in an important [early AI paper from 1968](https://courses.cs.umbc.edu/471/spring23/02/resources/MI3-Ch.10-Amarel.pdf) by Saul Amarel, as the (regrettably named) "missionaries and cannibals problem". Amarel's paper built on earlier research into search-based problems by giving a formal way of defining planning problems.


## States

At each step of the solution, we care about the number of humans and robots on each side, plus the position of the boat . This configuration is the ***state***. In general, a planning problem consists of a collection of *things* (people, machines, items, switches, variables, etc.) that we want to manipulate into a desired configuration. The state describes the current values of all the relevant things.

Planning problems have a *starting state* that represents the initial configuration and a *goal state* that represents the desired ending condition. For us, the starting state is the condition with all humans, robots, and the boat on one side of the river:
```
  HHH RRR
~~~~~~~~~~~~
     B

~~~~~~~~~~~~
```
The goal state has everything on the opposite side of the river:
```
~~~~~~~~~~~~
     
     B
~~~~~~~~~~~~
  HHH RRR
```
The ***state space*** is the set of all possible valid states that can exist within a particular problem. That is, it's all the ways we can position the humans, robots, and the boat without violating the rule about the numbers of humans and robots.

## Successor states

Suppose that we have a particular state, which we'll denote as *x*. We can define the set of *actions* that are permissible to take in that state. For example, suppose that we have the following state for the river problem:
```
   HH RR
~~~~~~~~~~~~
     
     B
~~~~~~~~~~~~
    H R
```
One valid action is to move the human from the south side to the north side. Observe that moving the robot would result three robots vs. two humans on the north side, which is impermissible. The *successor states* of *x* are the states that are one action away from *x*. In our current example, the successor state would be
```
  HHH RR
~~~~~~~~~~~~
     B
     
~~~~~~~~~~~~
      R
```
The other valid action is to move both the human and robot back to the north side, which would bring us back to the starting state:
```
  HHH RRR
~~~~~~~~~~~~
     B
     
~~~~~~~~~~~~
```

### Practice question

> Consider the initial configuration for the river problem. What valid actions can you take? Work out all of the successor states to the initial configuration.

## Formal definition

A search problem has the following elements:

- *S*, the state space for the problem

- *A*, the set of possible actions

- An initial state *i ∈ S*

- A goal state *g ∈ S*

- *actions(s)*, a function that returns the set of actions that are possible in state *s ∈ S*. Note that this may be the same as the complete action set *A*, or a subset of *A* if only some actions are possible from *s*.

- *successors(s)*, a function that returns the set of states obtained by applying *actions(s)* to *s*

For now, we're interested in identfying a sequence of actions that move from state *i* to state *g*. We're not necessarily requiring the "best" or "most efficient" solution (however we might define those), just *some* plan that solves the problem.

Some problems have a cost function, *cost(s, a)*, that returns the cost of applying action *a* in state *s*. If it exists, the cost function captures the fact that some actions are more difficult or expensive that others, and we're usually interested in finding a plan with low total cost. We'll consider cost-aware search problems in the next unit.



## The general solution strategy

The key to solving planning problems is to **explore the state space**.

- Begin with the starting state
- Generate all of its successor states and store them
- Choose one stored state and generate *its* successors and store them
- Continue this process until you either reach the goal state or have no more stored states to explore, which would indicate there is no feasible plan

"But wait!", you shout. "That's way too vague."

You're right. The top-level description of this process leaves a lot of things undecided:

- How to represent the states?
- How to store the unprocessed states during the search?
- How to choose the next state to expand?
- How to keep track of states that have already been expanded so we don't get stuck in a loop?

Here's a key point that will come up repeatedly throughout this course: Choosing to use a certain method, like state search, isn't the hard part of solving a problem. The hard parts are working out the practical details of how to represent the problem, generate successors, and choose the next state to expand.

## Representing states

For the river problem, we care about the number of humans and robots on each side and the position of the boat. We could represent the state using three values:

- The number of humans on the north bank
- The number of robots on the north bank
- A boolean to specify if the boat is on the north bank

With this setup, the starting state would be `(3, 3, True)`. The goal state would be `(0, 0, False)`. Moving humans or robots from the north bank to the south subtracts from their corresponding numbers and toggles the state of the boat. Likewise for moving from the south to the north.

### Practice problem

> For the starting state, apply the possible actions and generate the successor states using the notation above.


There are three possible actions we can take from the starting state:

- Move one human and one robot. The result is `(2, 2, False)`.
- Move one robot. The result is `(3, 2, False)`.
- Move two robots. The result is `(3, 1, False)`.

We can't move one or two humans because those actions would leave the remaining human(s) outnumbered on the north bank.

Suppose we choose to expand the `(2, 2, False)` state next.
```
   HH RR
~~~~~~~~~~~~
     
     B
~~~~~~~~~~~~
    H R
```

There are two possible moves:

- Move the human back to the north bank to get `(3, 2, True)`
- Move both the human and robot back to get `(3, 3, True)`, returning to the start state

## Search tree

You can represent the search process as a tree with the initial state as the root, its successors as children, and so forth.
```
                                     (3, 3, True)
                                          |
                                          |
                         -----------------------------------
                        |                 |                 |
                   (2, 2, False)     (3, 2, False)     (3, 1, False)
                        |
                        |
              ---------------------
             |                     |
        (3, 2, True)          (3, 3, True)
```

### Practice problem

Work out the rest of the second level of the tree by expanding the other two nodes on the first level.

## Solve

Work out the solution to the puzzle, then write out the solution plan using the three-value notation.


