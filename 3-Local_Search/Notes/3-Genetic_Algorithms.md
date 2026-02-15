# Genetic Algorithms

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Gustav_Klimt_032.jpg/960px-Gustav_Klimt_032.jpg" width="300px" />

*Tree of Life, Stoclet Frieze*, Gustav Klimt (1909)


## Overview

Charles Darwin published *On the Origin of Species* in 1859. One of the most important books in scientific history, it proposed the theory of evolution by natural selection as the dominant explanation for the diversity of life and a unifying concept underlying all of biology. Some concepts of evolutionary theory existed in natural science before Darwin's time, but they were mostly speculative and the mechanism of change was not well-understood. Darwin explained how natural selection of heritable traits leads to gradual, continuous change within populations, and marshalled an overwhelming amount of evidence for his theory based upon twenty years of research. *On the Origin of Species* also supported the then-radical concept of the branching descent of all species from a common ancestor - the Tree of Life.

Genetic algorithms apply the concept of survival-of-the-fittest to optimization. The method maintains a "population" of candidate solutions. At each step, the best current individuals, as determined by a fitness function, are used to produce a new population of candidates that should, on average, have higher fitness. The process of producing the next generation uses genetic concepts of selection, crossover, and mutation.

## Procedure

The basic genetic algorithm procedure starts with an initial population of random solutions and then does the following steps in each generation:

- Score the fitness of each member of the current population
- Randomly select two "parent" solutions, weighted by their fitness so that more fit individuals are more likely to be chosen
- Use those two parents to generate "child" solutions using the genetic crossover procedure, described below
- Probabilistically apply some mutations to the children to add variation
- Repeat the parent selection, crossover, and mutation steps until the next generation is full
- Optionally, preserve the current highest scorers unaltered into the next generation to maintain the strongest solutions

```
Genetic Algorithm

inputs:
    f, the fitness function
    max_generations, the number of iterations to run

outputs:
    the solution of highest fitness at the end of the procedure

population = {initial population of randomized solutions}

for generation = 1 to max_generations {

    // Calculate fitness of each candidate
    for individual in population {
        fitness[individual] = f(individual)
    }

    // Build the next generation
    next_population = {}
    while size(next_population) < size(population) {

        // Select two parents, biased toward higher fitness
        parent1 = selection(population, fitness)
        parent2 = selection(population, fitness)

        // Create two offspring by combining parents
        child1, child2 = crossover(parent1, parent2)

        // Randomly mutate each child to maintain diversity
        child1 = mutation(child1)
        child2 = mutation(child2)

        // Add children to the next generation
        add child1, child2 to next_population
    }

    // Optionally preserve the best individual(s) from the current generation (elitism)
    next_population = replace_worst(next_population, best(population, fitness))

    // Advance to the next generation
    population = next_population
}

// Return the individual with the highest fitness in the final population
return best(population, fitness)
```

As with our previous search methods, the challenge of genetic algorithms isn't in deciding to use a genetic algorithm, it's in implementing the specific details: the solution encoding, the fitness function, and the selection, crossover, and mutation procedures.


## Chromosomes

The starting point for a genetic algorithm is to encode the solution as a "chromosome" vector. Traditionally, these are binary vectors, but vectors of integers are also common.

For example, in the 0/1 knapsack, a solution is a sequence of 0/1 values that encode whether each item is taken or not taken. This is a natural fit for a genetic algorithm: each chromosome is the sequence of bits for one candidate solution. In a problem with ten items, for example, the solution that takes odd-numbered items could be encoded as `0101010101`, if we consider the first item to be *x*<sub>0</sub>.

If the solution to the problem is a vector of integers, they can be used directly, or encoded in binary. For example, `[3, 5, 7]` could be encoded as the binary string `011 101 111`

### Tricky binary encodings

Here's a subtle point about binary encodings. Consider the 0/1/2 knapsack problem, where you can take 0, 1 or 2 of each item. You could construct a binary encoding by allocating two bits for each item as follows:

- `00`: take 0 of the item
- `01`: take 1
- `10`: take 2

For example, a solution vector for a four-item problem might be `[0, 1, 1, 2]`, which would correspond to the binary encoding, `00 01 01 10`.

What about the fourth bit combination, `11`? It corresponds to taking 3, but that's not allowed for the problem. If you use the two-bit encoding, you have to decide how to handle the invalid `11` bit combination. Options are to map it to a solution value of 0, or implement the later steps of the method so that `11` values can't occur.

## Fitness

The optimization is driven by a *fitness function*. Given a chromosome, the fitness function returns a quantitative measure of its quality. For the 0/1 knapsack problem we might use a fitness function like the following (in pseudocode):
```
// Return fitness of candidate binary chromosome chr
fitness(chr) {

    // Locations where chromosome is 1
    selected = indices(chr == 1)

    // Sum weights of included items
    total_weight = sum(weights[selected])

    // Reject solutions that exceed capacity
    if total_weight > capacity {
        return -infinity
    }

    // Return value of included items
    else {
        return sum(values[selected])
    }
}
```
Notice that over-capacity solutions return `-infinity` not 0. An over-capacity solution is infeasible and therefore worse than an empty knapsack.

## Selection

The main genetic step selects two "parent" chromosomes and uses them to generate two new "child" chromosomes that will be part of the next generation.

The selection procedure is weighted by fitness, so that higher-performing members of the population are more likely to be selected. A standard method is *roulette wheel* selection, where parents are chosen randomly and the probability of selection is proportional to fitness.

Suppose that we have three candidates with fitness scores of 2, 4, 5 and 9. The total fitness of the population is 20. The selection procedure generates a random number and uses it to choose the parent as follows:

- Candidate 1 is selected with probability 2/20
- Candidate 2 is selected with probability 4/20
- Candidate 3 is selected with probability 5/20
- Candidate 4 is selected with probability 9/20

This sample is done ***with replacement***, so that an individual can be chosen multiple times. This makes sense: it mimics the idea of higher fitness individuals having greater opportunities for reproduction. Also notice that under this scheme the two selected parents can actually be the same individual.

Another option is [tournament selection](https://en.wikipedia.org/wiki/Tournament_selection).

## Crossover

Suppose that the selection step has chosen the following two parents, which are encoded as binary strings:
```
parent_1 = 001010011
parent_2 = 100101110
```
The crossover step picks a random *crossover point* to split the parents and then exchanges their left and right sides to create two children, each with part of the chromosome material of each parent.

For example, if the random crossover position is 4, we'd split the parents into two parts: the first four bits and the last five bits.
```
  parent_1         parent_2
  --------         --------
0010 | 10011     1001 | 01110
```
Notice that there's one crossover point that applies to both parents.

The method then combines the left side of one parent with the right side of the other to create a child solution:
```
  parent_1         parent_2
  --------         --------
0010 | 10011     1001 | 01110
----                    -----
  |                       |
  |                       |
   -----        ----------
        |      |
        v      v 
      0010 | 01110
```
The second child is constructed from the other pair:
```
  parent_1         parent_2
  --------         --------
0010 | 10011     1001 | 01110
       -----     ----
         |        |      
       --|-------- 
      |   ----
      |       |
      v       v
     1001 | 10011
```
Notice that, in both cases, the left side of the parent becomes the left side of the child and likewise for the right side. Never use the right side of a parent as the left side of a child!

The result is two new vectors:
```
child_1 = 001001110
child_2 = 100110011
```
This process repeats until the next generation is filled.

## Mutation

After children are constructed, apply a per-bit mutation with a small probability. This step mimics real-world mutation by adding unexpected genetic diversity to the population.
```
// Apply per-bit mutation to the input chromosome
mutation(chr) {
    for i = 1 to length(chr) {
        if random() < MUTATION_PROB {
            chr[i] = ~chr[i]  // bit flip
        }
    }
}
```
Notice that this is a **per-bit** operation. Every bit has an independent probability of being flipped. `MUTATION_PROB` is small, like .01 or .001.

## Elitism

An optional variation is to promote a small number of top performers (perhaps 1-2% of the total population) unchanged to the next generation. This variation keeps high performing chromosomes in the pool so they remain available for the next generation.
