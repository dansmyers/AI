# Local Search

## Overview

**Under construction**. The content here is likely to change. Don't work on anything yet.

## Topics

- Objective functions
- Local vs. global minima and maxima
- Hill-climbing search
- Simulated annealing
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

