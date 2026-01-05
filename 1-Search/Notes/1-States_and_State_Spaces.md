# States and State Spaces


## A river crossing problem

You've probably seen riddles that involve taking objects across a river, like the one about the farmer who needs to transport his chicken, grain, and fox. Here's another one that we'll use for our starting example.

> A group of three AI researchers and three robots needs to reach the other side of a river. Their boat can only carry at most two entities at a time (two humans, two robots, or one of each, or a single human/robot). Unfortunately, the ethical control units of the robots are still a bit misaligned, so the robots can never be allowed to outnumber the humans on either side of the river at any time.
>
> Formulate a plan to move everyone to the other side of the river without provoking a robot uprising.

This problem was considered in an important [early AI paper from 1968](https://courses.cs.umbc.edu/471/spring23/02/resources/MI3-Ch.10-Amarel.pdf) by Saul Amarel, as the (regrettably named) "missionaries and cannibals problem". Amarel's paper gave a formal way of defining planning problems that could be solved by search algorithms.


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
The only valid action is to move the human from the south side to the north side. Observe that moving the robot would result three robots vs. two humans on the north side, which is impermissible.

The *successor states* of *x* are the states that are one action away from *x*. In our current example, the successor state would be
```
  HHH RR
~~~~~~~~~~~~
     B
     
~~~~~~~~~~~~
      R
```

### Practice question

Consider the initial configuration for the river problem. What valid actions can you take? Work out all of the successor states to the initial configuration.

## Formal definition

A search problem has the following elements:

- *S*, the state space for the problem

- An initial state *i ∈ S*

- A goal state *g ∈ S*

- *actions(s)*, a function that returns the set of actions that are possible in state *s ∈ S*

- *successors(s)*, a function that returns the set of states obtained by applying *actions(s)* to *s*


- *cost(s, a)*, a function that returns the cost of applying 



## Representing states




## The general solution strategy

The key to solving planning problems is to **explore the state space**.

- Begin with the starting state
- Generate all of its successor states and store them
- Choose one stored state and generate *its* successors
- Continue this process until you either reach the goal state or have no more stored states to explore, which would indicate there is no feasible plan

"But wait!", you shout. "That's way too vague."

You're right. The top-level description of this process leaves a lot of things undecided:

- How to represent the states?
- How to store the unprocessed states during the search?
- How to choose the next state to expand?
- How to keep track of states that have already been explored so we don't get stuck in a loop?






