# Satisfiability

## Overview

Boolean satisfiability is one of the most important constraint satisfaction problems in theoretical computer science. The general satisfiability problem, often abbreviated as **SAT** is as follows: 

- Given a set of Boolean variables *x*<sub>1</sub>, *x*<sub>2</sub>,..., *x*<sub>*n*</sub>,
- and a Boolean expression that uses those variables,
- determine an assignment of true/false values that makes the formula true, or verify that no such assignment exists.

For example, consider the formula

$$ (x_1 \vee x_2) \wedge (\not x_1 \vee \not x_2 \vee x_3) \wedge (\not x_3) $$

One possible satisfying assignment is (false, true, false).
