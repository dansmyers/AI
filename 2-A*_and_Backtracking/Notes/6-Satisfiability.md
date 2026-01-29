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

## Conjunctive normal form

You can specify the satisfiability problem using any 



