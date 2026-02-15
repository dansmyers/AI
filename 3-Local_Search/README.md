# Local Search


<img src="https://preview.redd.it/hungry-ghost-trapped-in-a-jar-v0-641pzke2r5dg1.png?auto=webp&s=483e7fc7359ec9344af7f06ebda0521c1eb8caec" width="500px" />

*This military drone swarm is controlled by a hungry ghost trapped in a jar? This hungry ghost trapped in a jar does my taxes? My therapist is a hungry ghost trapped in a jar?*


## Deliverables due and in-class quiz: 2/27



## Overview

Our two previous units covered variations of *tree search*, where we explored the space of problems states searching for an optimal plan that connected a starting state to a desired goal.

This unit introduces one more family of search techniques: **local search**. Unlike tree search, these methods don't maintain a frontier of states that are waiting to be explored. Instead, we simply move from the start state to a neighbor, then to the next neighbor, and so forth, until the search satisfies a stopping criterion. These methods are used for general optimization problems, where there isn't a specific goal state, but there is an objective function that we desire to maximize or minimize.

Combinatorial optimization problems - where you're trying to pick the best collection of things - are often well-suited to local search.

The second major topic for this unit is **dynamic programming**, an important algorithmic concept that is often used to find exact solutions to combinatorial problems. Dynamic programming is broader than AI, but it's a fundamental building block of many advanced algorithms, so I include it here so you'll have a chance to practice it even if you don't take an advanced algorithms course.

The third topic is reading about **specs-driven development**. This is the formalization of the development procedure we've been doing so far: chat about a problem to develop a specification document, then develop that into a detailed implementation with step-by-step tasks and tests.


## Topics

- Objective functions
- Local vs. global minima and maxima
- Hill-climbing search
- Simulated annealing
- Beam search
- Genetic algorithm concepts: populations, fitness, crossover, mutation
- Particle swarm optimization
- Recursively formulating dynamic programming problems
- The bottom-up solution strategy for DP problems
- Example problems: 0/1 knapsack, rod cutting, edit distance, longest increasing subsequence
- Determining the complexity of a bottom-up DP algorithm
- More on the spec-driven development approach

 
## Resources

### Dynamic programming

- Start with [this article I wrote](https://dansmyers.substack.com/p/supermarket-sweep-an-introduction) that gives an overview of the concept and looks at two canonical problems: 0/1 knapsack and rod cutting.

- Then read [this article](https://dansmyers.substack.com/p/algorithms-201-levenshtein-edit-distance) on the Levenshtein edit distance.
 
- Here's [a third article](https://dansmyers.substack.com/p/algorithms-201-longest-increasing) on the longest increasing subsequence problem. Focus on the first part, which describes the *O*(*n*<sup>2</sup>) solution. The second part describes an *O*(*n* log *n*) solution that is interesting, but wonky; it's optional if you're interested, but not required.

### Local search and genetic algorithms

- Read my notes in the directory above

- [The Berkeley textbook section](https://inst.eecs.berkeley.edu/~cs188/textbook/search/local.html) is also good

### Specs-driven development

- Read the first half of [this description from GitHub](https://github.com/github/spec-kit/blob/main/spec-driven.md). It gives a good overview of the motivation and concept for spec-driven development. The second part goes over some commands for a specific library they've built that are not important for us.

- [Spec-driven development doesn't work if you're too confused to write the spec](https://publish.obsidian.md/deontologician/Posts/Spec-driven+development+doesn't+work+if+you're+too+confused+to+write+the+spec). Makes the important point that much of coding is making arbitrary but binding choices about how things will be represented/named/encoded so they can be processed by the application logic, then shoving data around between those various representations. The spec has to provide enough information to help the model understand these representations, or you end up with systems that have incompatible parts. This ties into why we talk so much about encapsulation, with clear boundaries and well-defined interfaces between components.

- Listen to the first half of [this podcast](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code) with Lazar Jovanovic (*professional vibe coder*). There is some chit-chat, but he gets into a great overview of the process of prototyping, then building specifications, then turning them into detailed plans.

