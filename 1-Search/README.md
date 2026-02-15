# Sprint 1: Solving Problems by Searching

<img src="https://user-images.githubusercontent.com/775050/62004829-79b29400-b12a-11e9-98f7-45de227e8c73.png" width="400px" />

*SHRDLU, created by Terry Winograd in the early 1970s, was an important early AI system. SHRDLU used a model "blocks world" with blocks of different sizes, shapes, and colors arranged on a table. The system had the ability to take commands in natural language, solve planning problems to rearrange the blocks into a desired configuration, and answer questions about their spatial relationships. The name SHRDLU comes from the printing industry. The old hot type printing systems organized letters in frequency order, which led to ETAOIN SHRDLU becoming a nonsense phrase that was sometimes accidentally printed in newspapers.*

## Deliverables due and in-class quiz: 1/30

## Overview

In 2019, the AI researcher Rich Sutton wrote a short blog post that's become famous in the AI field, ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html). In it, he argues that progress in AI has come not from humans developing more sophisticated algorithms and domain-specific problem-solving techniques, but instead from **more computation**. As Moore' Law has increased the amount of computational power available to AI systems, the complexity of problems that researchers have been able to solve has also increased. 
>Seeking an improvement that makes a difference in the shorter term, researchers seek to leverage their human knowledge of the domain, but the only thing that matters in the long run is the leveraging of computation.
This is the bitter lesson: In the long run, progress in AI has almost always been due to scaling up general methods with more compute, rather than crafting sophisticated domain-specific algorithms.

Sutton says that the two most important general-purpose algorithms are *search* and *learning*, because they benefit directly from increasing computational power:
>One thing that should be learned from the bitter lesson is the great power of general purpose methods, of methods that continue to scale with increased computation even as the available computation becomes very great. The two methods that seem to scale arbitrarily in this way are search and learning.

These are going to be the themes of our class. In the first half, we'll look at searching - the core technique of classical AI. The second half will focus on machine learning, neural networks, and language models.

For the first sprint, we're going to start by solving planning problems using **state-based search**. We'll talk about how to represent as a sequence of states, and then use structured search techniques to explore the graph of state relationships, with the goal of finding an efficient plan to move from a starting state to a goal. After this unit, we'll look at variations on the basic search idea: constraints and logic problems, heuristics, and adversarial game-playing.


## Topics

- Representing problems as state spaces
- The basic tree search algorithm
- Breadth-first and depth-first searching
- Iterative deepening
- Uniform-cost search
- Returning the history of actions leading to the solution
- Examples of standard planning problems

## Deliverables

Complete the projects in the `Deliverables` directory

## Resources

Materials for this unit are pretty minimal:

- Start with my notes on the basic concepts in the `Notes` directory.

- After you've read those, look sections 1.1-1.3 of the [free Berkeley AI text](https://inst.eecs.berkeley.edu/~cs188/textbook/search/). We'll return to this book over the course of the semester.

- If you'd like to see a video discussion of the breadth-first and depth-first search algorithms, [this one is pretty good](https://www.youtube.com/watch?v=pcKY4hjDrxk).
