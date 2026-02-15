# Simulated Annealing

<img src="https://donoughe.com/wp-content/uploads/2018/02/WhiteHotSteel-copy-2000.jpg" width="400px" />

*White Hot Steel*, Ron Donoughe ([link](https://donoughe.com/portfolio-items/white-hot-steel/?portfolioCats=44))

## Overview

Simulated annealing is a variation of the hill-climbing search that allows the search to occasionally make moves that are neutral or negative to break out of local minima.

The term *annealing* comes from metalworking and refers to heating a metal and then cooling it slowly. Heat puts energy into the metal's atoms, which allows them to move around a bit within the metal's chemical lattice structure. Cooling gradually settles the atoms back down into a lower energy state, which results in a better crystalline structure that makes the metal easier to work.

Simulated annealing starts the search with a "high energy" state where lots of random moves are allowed. Over time, it transitions to a "low energy" state where random moves are harder to make, which eventually transitions into pure hill climbing to finish the search. The rate of transition from high- to low- energy is governed by a function called the *cooling schedule*.

## Pseudocode

```
Simulated Annealing

// Initialization
s = starting state

// Annealing loop
for t = 1 to infinity {

    // Current cooling schedule value
    a = schedule(t)

    // Stopping condition: search has finished
    if a == 0 {
        return s
    }

    // Choose a random neighbor
    neighbor = random_successor(s)

    // Change in objective value
    delta = f(neighbor) - f(s)

    // If neighbor is better, accept the move
    if delta > 0 {
        s = neighbor
    }

    // else, accept worse moves with a probability depending on delta and a
    else if random() < exp(delta / a) {
        s = neighbor
    }
}
```
The most complex line is
```
else if random() < exp(delta / a) {
```
This line calculates a probability of accepting the move using the exponential function, `exp(delta / a)`. If `delta` is negative - that is, the neighbor is worse than the current state - then the probability of accepting the move decreases exponentially as `delta` increases. This has the following effects:

- Moves that are worse than but close to the current state are easier to accept than moves that are significantly worse
- If `a` is large, then the numerator is close to 0, which makes the exponential close to 1 and makes all moves easier to accept
- If `a` is close to 0, the numerator becomes large, which makes the exponential close to zero and makes all moves harder to accept

## Cooling schedule
It turn out that if `schedule(t)` decreases slowly enough this method almost always works, but the required cooling may take too many iterations to be practical. There are no fixed rules for choosing the cooling schedule. Advanced versions can use an adaptive approach where the temperature is adjusted dynamically based on how the search is progressing.
