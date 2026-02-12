# Evolving Blackjack Strategy

<img src="https://upload.wikimedia.org/wikipedia/commons/5/59/Salon_d%27Or_Firth.jpg" width="600px" />

*Salon d'Or, Homburg*, William Powell Frith (1871)

[I also like to live dangerously.](https://www.youtube.com/watch?v=JVwEf7xSjwY)

## Overview

*Blackjack*, sometimes known as 21, is the most popular table game played in American casinos. The object is to obtain a hand of cards that scores higher than the dealer's hand without going over a score of 21.

In this project, you're going to use genetic programming to **evolve a strategy for blackjack**. Your strategy will specify under what circumstances the player should hit or stand. You'll score the fitness of each strategy by playing simulated hands of blackjack, then use the genetic algorithm technique to evolve new strategies that descend from the current top performers. The overall goal is to evolve a strategy that performs close to the theoretically optimal win rate of approximately 49.5%.

## Disclaimer

These projects are for educational purposes only. They are not an endorsement of the extremely cool vice of gambling.

## Rules

If the rules of blackjack aren't familiar to you, first spend some time learning the game. I recommend the [rules summary](https://wizardofodds.com/games/blackjack/basics/) from the Wizard of Odds, my go-to source for gaming knowledge. You can ask Claude to code a practice game for you.

Our version will only allow the player to **hit or stand**. We won't consider alternative moves like doubling, splitting or surrendering, or side best like insurance. This means that at every decision in the game is a binary choice to either hit or stand.

For this project, we're going to focus on *single-deck blackjack*, which is generally more favorable to the player. Most Vegas casinos now play -with 6 or 8 decks shuffled togehter to reduce the impact of card counting (more on that in the next project).

## Basic strategy

<img src="https://wizardofodds.com/blackjack/images/bj_1d_s17.gif" width="300px" />

The Wizard's basic blackjack strategy is given in the table above. Observe that each entry corresponds to a player hand value and the dealer's face-up card. For example, if the player has a hand value of 12, he should hit if the dealer shows a 2 or 3, stand if the dealer has a 4-6, and hit on all higher-valued cards.

The second table is for "soft" hands where the player has an 11-valued Ace. These can be played more aggressively, since it isn't possible to bust by hitting a soft hand - if the player draws a card that would make the score greater than 21, then the value of the Ace changes to 1. 

The tables specify cases where the player should double or retire if allowed; we're not implementing these options, so these should revert to the basic hit/stand choices.

The third table is for paired hands. Many casinos allow the player to "split" pairs, doubling the bet to play two hands. We're not implementing splitting, so ignore this table.

## Description

### Objective

Evolve a playing strategy that determines whether to hit or stand based on the player's current hand total and the dealer's face-up card. The goal is to discover a strategy that approaches the theoretical optimum (approximately 49.5% win rate).

You're going to produce a genetic algorithm optimizer wrapped around a blackjack simulation engine. The GA evolves a population of strategy chromosomes, evaluates their fitness through simulated play, and iteratively improves the population over generations.

### Game rules

The simulation uses standard blackjack rules with the following specifications:

- Each hand is dealt from a freshly shuffled standard 52-card deck
- Dealer stands on soft 17
- Player may only hit or stand (no doubling, splitting, or insurance)
- A tie (push) counts as 0.5 wins
- Blackjacks (natural 21) count as wins


### Strategy encoding

Each individual in the population encodes a complete playing strategy as a binary chromosome. The strategy must account for both hard hands (no ace, or ace counted as 1) and soft hands (ace counted as 11).

The hard hands state space consists of 170 bits:

- Player hand totals: 4 through 20 (17 values)
- Dealer up card: Ace through 10 (10 values)

The soft hand state space is 90 bits:

- Player hand totals: Soft 12 through soft 20 (9 values, corresponding to A-A through A-9)
- Dealer up card: Ace through 10 (10 values)

This yields a 260-bit chromosome where each bit represents the decision for one player-dealer combination:

- 0 = Stand
- 1 = Hit

### Fitness function

Fitness is calculated by simulating 1,000 hands of blackjack using the individual's encoded strategy. The fitness of a strategy is the fraction of hands it wins, accounting for ties as a partial win:
```
fitness = (wins + 0.5 × ties) / (wins + losses + ties)
```

### Procedure

Start by initializing a population of 100 random 260-bit strategy vectors. Think about how to represent these so you can access the internal bits efficiently.

Run 50-100 generations of evolution. For each generation:

- Evaluate the fitness of each strategy vector by using it to simulate 1000 hands of blackjack according to the rules above
- Perform genetic algorithm evolution on the population of strategy vectors to create the next generation

You can play around with settings for the GA. Some reasonable starting points are:

- Roulette wheel selection weighted by fitness (higher fitness individuals are more likely to be selected)
- Single-point crossover between pairs of selected individuals
- Mutation rate of .01 per bit
- Top 2 individuals advance unchanged to the next generation

### Output

Produce two figures:

- A line plot showing the fitness on the vertical axis vs. generation on the horizontal axis. Plot lines showing the change in min, max, median, and mean fitness. Ideally, this should show convergence towards a value a little less than 50%.

- A strategy matrix similar to the one above. For each combination of player hand and dealer card, report the percentage of individuals in the final population that recommend hitting in that situation. You should see that the recommendations to hit or stand agree with those in the basic strategy. Use a heat-map visualization: cells with 100% hit should be colored pure red, 100% stand should be colored pure blue, with fractions shading between the two colors.
