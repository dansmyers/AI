# Satisfiability

<img src="https://i.discogs.com/Hyz_O2vakSGGguvFpqmxxWPvyh_Li0J6pCGAzis9DJo/rs:fit/g:sm/q:90/h:527/w:522/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTI0NTk2/MzQtMTI4NTI1NDY4/OC5qcGVn.jpeg" width="300px" />

*Extremely predictable header image choice*, via [Discogs](https://www.discogs.com/release/2459634-Rolling-Stones-Satisfaction)

## Overview

Boolean satisfiability is one of the most important constraint satisfaction problems in theoretical computer science. The general satisfiability problem, often abbreviated as **SAT** is as follows: 

- Given a set of Boolean variables *x*<sub>1</sub>, *x*<sub>2</sub>,..., *x*<sub>*n*</sub>,
- and a Boolean expression that uses those variables,
- determine an assignment of true/false values that makes the formula true, or verify that no such assignment exists.

For example, consider the formula

$$ (x_1 \vee x_2) \wedge (\lnot x_1 \vee \lnot x_2 \vee x_3) \wedge (\lnot x_3) $$

One possible satisfying assignment is (false, true, false).

### Notation

It might have been a while since you've seen logical notation.

- $$\wedge$$ is the logical-AND operator, or *conjunction*
- $$\vee$$ is the logical-OR operator, or *disjunction*
- $$\lnot$$ is the logical-NOT operator, or *negation*

### Importance

SAT has practical applications, particularly in constraint modeling, formal verification, and circuit validation, which shows up in computer design.

For theoretical computer scientists, SAT has an important place in complexity theory. It was one of the first problems proved to be **NP-Complete**, and theoretical computer scientists working in complexity theory use SAT (or more commonly one of its variations, discussed below) as a baseline problem when performing complexity comparisons. [See my old notes from the COVID era](https://github.com/dansmyers/Algorithms/blob/master/Challenge_Projects/2-The_Lost_Sprint.md) for more detailed background on NP-completeness. It's not required reading for this unit, but it is cool.

## Conjunctive normal form

You can specify the satisfiability problem using any boolean formula you like. In practice, however, it's common to work with a restricted version called **conjunctive normal form** (CNF). A SAT-CNF formula has the following form:

- A *literal* is a variable or the negation of a variable, such as $$x_1$$, $$\lnot x_3$$, etc.

- A *clause* is a disjunction (logical-OR) of literals, such as $$(x_1 \vee \lnot x_3 \vee x_5)$$

- A formula is a conjunction (logical-AND) of clauses, such as $$(x_1 \vee \lnot x_3 \vee x_4) \wedge (\lnot x_1 \vee x_2) $$

Therefore, the basic SAT-CNF problem is to find an assignment that makes every clause true, such that the AND of all clauses is also true.

### 2-CNF-SAT
**2-CNF-SAT** is a more restricted version that restricts each clause to having exactly two literals. For example,

$$(x_1 \vee \lnot x_2) \wedge (\lnot x_1 \vee x_3) \wedge (\lnot x_2 \vee \lnot x_3) $$

2-SAT-CNF version can be solved in polynomial time.

### 3-CNF-SAT

The **3-CNF-SAT** problem requires each clause to have three literals. For example,

$$(x_1 \vee \lnot x_2 \vee x_4) \wedge (\lnot x_1 \vee x_3 \vee \lnot x_5) \wedge (\lnot x_2 \vee \lnot x_3 \vee x_4) $$

3-CNF-SAT is the most common form used in theoretical computer science.

- Unlike the 2-literal version, it's NP-complete. This small shift, where moving from two variables to three radically changes the complexity of the problem is the kind of thing that drives theorists bonkers (in a good way).

- It's not obvious, like at all, but it turns out that *any* boolean satisfiability problem [can be transformed](https://en.wikipedia.org/wiki/Tseytin_transformation) into an equisatisfiable 3-CNF-SAT version in polynomial time. That is, the 3-CNF version has the same satisfiability result as the original formula.







