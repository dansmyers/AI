# States and State Spaces


## River crossing problem

You've probably seen riddles that involve taking objects across a river, like the one about the farmer who needs to transport his chicken, grain, and fox. Here's another one that we'll use for our starting example.

> A group of three AI researchers and three robots needs to reach the other side of a river. Their boat can only carry at most two entities at a time (two humans, two robots, or one of each, or a single human/robot). Unfortunately, the ethical control units of the robots are still a bit misaligned, so for safety there can never be humans outnumbered by robots on either side of the river at any time.
>
> Formulate a plan to move everyone to the other side of the river without provoking a robot uprising.
>
> Clarifications:
>
> - It's permitted to leave robots alone with no human supervision
> - Robots don't care if a human is in the boat vs. on the bank

This problem was considered in an important [early AI paper from 1968](https://courses.cs.umbc.edu/471/spring23/02/resources/MI3-Ch.10-Amarel.pdf) by Saul Amarel, as the (unwokely named) "missionaries and cannibals problem". Amarel's paper built on earlier research into search-based problems by giving a formal way of defining planning problems.


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
The ***state space*** is the set of all possible valid states that can exist within a particular problem. That is, it's all the ways we can position the humans, robots, and the boat without violating the requirements of the problem.

## Successor states

Suppose that we have a particular state, which we'll denote as *x*. We can define the set of *actions* that are permissible to take in that state. For example, suppose that we have the following state for the river problem:
```
   HH RR
~~~~~~~~~~~~
     
     B
~~~~~~~~~~~~
    H R
```
One valid action is to move the human from the south side to the north side. Observe that moving the robot would result three robots vs. two humans on the north side, which is impermissible.

Taking an action generates a new state. The *successor states* of *x* are the states that are one action away from *x*. In our current example, the successor state for that action would be
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

The goal of the search problem is to identify a sequence of actions that move from state *i* to state *g*.


### Cost functions and optimality

Some problems have a cost function, *cost(s, a)*, that returns the cost of applying action *a* in state *s*. If it exists, the cost function captures the fact that some actions are more difficult or expensive that others. The river crossing problem doesn't have a cost.

If a cost function exists, we're probably going to be interested in finding the *optimal* plan: the one that achieves the goal with minimum cost. That's harder than simply identifying if a solution exists.

For now, we're only going to consider costless problems, so that optimality isn't a consideration. We just want *some* plan that solves the problem. We'll consider cost-aware search problems in a future note.


## The general solution strategy

The general approach to solving planning problems is to **explore the state space** in an organized way. The basic method is to repeatedly choose a candidate state and generate its successors:

- Begin with the starting state
- Generate all of its successor states and store them
- Choose one stored state, generate *its* successors, and store them
- Continue this process until you either reach the goal state or have no more stored states to explore, which would indicate there is no feasible plan

"But wait!", you shout. "That's way too vague."

You're right. The top-level description of this process leaves a lot of things undecided:

- How to represent the states?
- How to store the unprocessed states during the search?
- How to choose the next state to expand?
- How to keep track of states that have already been expanded so we don't get stuck in a loop?

Here's a key point that will come up repeatedly throughout this course: Choosing to use a certain method, like state search, isn't the hard part of solving a problem. The hard parts are working out the practical details, like how to represent the problem, generate successors, and choose the next state to expand.

## Representing states

Solving a problem using this method requires coming up with a representation for the important variables that determine the state. Ideally, this should be compact and allow you to easily generate successors.

There might be multiple options for how to encode the state for a particular problem. For example, we might start the river problem by trying to track the position of each human, robot, and the boat as a seven-element tuple. At the start of the problem, everything is on the north bank:
```
initial_state = (N, N, N, N, N, N, N)
```
The goal state would have everything on the south bank:
```
goal_state = (S, S, S, S, S, S, S)
```
If you think about it, though, this representation is not ideal. We don't care about the *individual* humans and robots, only the numbers of each on the two sides. Also, the seven-element vector makes it hard to generate successors, because you'd need logic for deciding which individual humans or robots to move on each step, which is unnecessarily complex.

Amarel's 1968 paper notes that it's sufficient to represent the state by keeping track of the number of humans and robots on a single bank and the position of the boat.  Therefore, we could reduce the essential details of the state to only three values:

- The number of humans on the north bank
- The number of robots on the north bank
- A boolean to specify if the boat is on the north bank

With this setup, the starting state would be `(3, 3, True)`. The goal state would be `(0, 0, False)`. Moving humans or robots from the north bank to the south subtracts from their corresponding numbers and sets the boat to False. Moving from the south to the north adds to the corresponding numbers and sets the boat to True.

### Practice problem

> For the starting state, apply the possible actions and generate the successor states using the notation above.


There are three possible actions we can take from the starting state:

- Move one human and one robot. The result is `(2, 2, False)`.
- Move one robot. The result is `(3, 2, False)`.
- Move two robots. The result is `(3, 1, False)`.

We can't move one or two humans because those actions would leave the remaining human(s) outnumbered on the north bank.

Suppose that we then choose to expand the `(2, 2, False)` state next.
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

## The general tree search method

The following pseudocode method will expand the search tree for a general planning problem until it finds the goal state or exhausts the state space of reachable nodes. It uses a data structure named `frontier` to store the set of discovered but unprocessed nodes and a set called `visited` to keep track of states that have been seen so we don't re-expand them.

```
Tree Search

input:
    initial state i
    goal state g
    successors function

output:
    success if the goal state is reachable, failure otherwise

initialize empty frontier structure

// Begin with the starting state
frontier.insert(i)

while frontier is not empty {

    // Choose the next state to expand
    x = frontier.pop()

    // If x is the goal state, we're done
    if x == g {
        output success and stop
    }

    // Check if x has already been visited; if so, don't expand it again
    if visited[x] {
      continue
    }

    // We're now visiting x, so mark it
    visited[x] = True

    // Generate successors of x
    s = successors(x)

    // Insert new unvisited successor states into frontier
    for j in s {
        frontier.insert(j)
    }
}  

// If the loop ends, the state space was exhausted without reaching the goal
output failure and stop
```

The choice of the frontier structure determines the order in which nodes are explored.

Notice that this version returns *success or failure* based on whether the goal state is reachable from the initial state. In practice, we'd usually like to have the actual sequence of actions and states required to reach the goal. We'll consider how to keep track of that history and some specific implementations of the tree search method later.

## Summary

State-based search is one of the core techniques of classical AI. The methods that we'll look at over the first part of the course are all elaborations of this basic idea, applied to progressively more complex problems. Therefore, make sure you understand the idea of representing problems as states, generating successors, and exploring the search tree as you're working through the rest of the material in this unit.



### Solve

Work out the solution to the puzzle, then write out the solution plan using the three-value notation.


