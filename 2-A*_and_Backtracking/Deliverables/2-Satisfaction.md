# Fun with Randomized 3-CNF-SAT

Soundtrack: [The Otis Redding version](https://www.youtube.com/watch?v=gmnZRBTPzg0) of (I Can't Get No) Satisfaction.

## Overview

In this project, you're going to play around with randomized versions of the 3-CNF-SAT problem and demonstrate evidence of its *phase transition* behavior. It turns out that the difficulty of a randomized 3-CNF instance isn't determined by the number of variables but by the **clause-to-variable** ratio.

- Problems with relatively few clauses for their number of variables (low ratio) tend to be *underconstrained*. There are few conflicts that make the problem difficult, so solvers are usually able to quickly identify a solution.

- Problems with a high ratio of clauses to variables are likely to have unsatisfiable conflicts and be *overconstrained*. The solver quickly prunes the solution space and discovers that there's no satisfying solution.

- There's a specific ratio at which the transition from "mostly satisfiable" to "mostly unsatistfiable" problems happens. We want to determine this ratio through empirical investigation.

You're going to experimentally investigate the behavior of randomized 3-CNF as a function of the clause-to-variable ratio. Along the way, you'll practice using Claude Code to develop a multi-step program where you have to validate correctness at each step.

## Experiment

Produce a graph showing the phase transition behavior of randomized 3-CNF-SAT.

The key parameter you'll be varying is *m*, the clause-to-variable ratio for the randomized 3-CNF instances.

- Fix the number of variables at **100**

- Generate a random instance of 3-CNF that has **100*m*** clauses. That is, if the clause-to-variable ratio *m* = 4, you would generate 400 clauses using the 100 variables. Information on the random generation process is given below.

- Try to solve the instance, again discussed in more detail below. Report the result as true or false.

- Repeat for 25 trials, recording the fraction of randomized instances that were solvable for the chosen value of *m*. 25 repetitions should give a smooth curve, but you can experiment with more if the curve seems too jumpy.

- Repeat for values of *m* from 1.0 to 8.0 in units of .25.

Your overall result will be a plot showing the fraction of solvable instances vs. *m*. You should see that low values of *m* have a high fraction of solvable instances and vice-versa. We're looking for the transition point where the phase change occurs.

### Parameters

The parameters above should be a good starting point. Once you have the experiment working, try increasing the number of trials to get a smoother estimate. You can also add upper and lower confidence limits around your data.

## Process

The key to this project is *developing incrementally* and testing as you go. Use Claude Code. I recommend that you start by chatting about the problem and producing a guiding document before you jump into generation.

### Randomized instances

Start by writing a fuction named `generate(n, m)`, where `n` is the number of variables and `m` is the desired clause-to-variable ratio.

- Determine the number of clauses
- Each clause has three literals, chosen *randomly* from the set of all variables *and their negations*
- There is no limit on how many times a variable can be chosen. Sample with replacement.

Think about how you're going to return the result! You'll need it in a form that the solver in the next step can use as input.

Before proceeding to the next step, test your generator and make sure it produces valid output. You can use Claude to help you automate this, but you must make sure that you're generating valid instances before moving to the next step.

You probably want to start by generating small problems to verify before scaling up to tens or hundreds of variables.

### Solver

Write a function named `solve` that takes a single problem instance as input and uses backtracking search to determine if it's satisfiable or not.

- There are lots of options for how to implement this

- You probably want to include some constraint propagation to speed up the process, but you don't have to do the fanciest options. Start with something simple, try it out, and scale up if you have to
  
- The only output you need is `True` or `False` to report whether the instance was satisfiable. You don't have to return the actual solution (altough you may want it for testing). Once you're running the real experiment, you'll want to minimize output.

Again, think about how you're going to test the solver. You'll probably want a combination of manual tests on small problems, but automated tests for bigger ones.

### Harness

Now build the overall experimental harness that calls the generator and solver in a loop for increasing values of *m*. This should be easy if you have the two previous parts working.

## Extensions

If you get the main experiment working, try increasing the number of variables to more precisely identify the exact value of *m* where the phase transition takes place.

Do some research on the problem. What do the theoretical results say?
