# Card Counting Strategy

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Caravaggio_%28Michelangelo_Merisi%29_-_The_Cardsharps_-_Google_Art_Project.jpg/1920px-Caravaggio_%28Michelangelo_Merisi%29_-_The_Cardsharps_-_Google_Art_Project.jpg" width="400px" />

*The Cardsharps*, Caravaggio (c. 1594)

## Overview

This project is the extension of the previous one. We're going to extend the basic blackjack strategy to include **card counting**.

We'll extend the genetic algorithm to include rules for counting the value of played cards and adjusting the size of the player's bet based on the current count. This requires making the simulation system and fitness evaluation more complex.


## Card counting basics

You've probably seen card counting depicted in movies with the idea that it's some sort of unbeatable gambling technique. This is not true. A perfectly executed card counting strategy *can* allow a player to overcome the house edge in blackjack, but the effective gains are small: around 1-1.5%. In practice, card counting blackjack requires a large bankroll and hundreds of hours of grinding play to realize meaningful gains.

Card counting isn't illegal, but casinos have the right to ban players they suspect are engaging in it. Part of the strategy of counting is applying it in a way that isn't blatantly obvious to casino managers.

The core idea of counting is simple: **A blackjack deck rich in ten-valued cards and aces is favorable to the player**. A deck rich in small cards is better for the dealer. Therefore, when the player knows the deck has a higher fraction of tens and aces, he should bet more. In advanced strategy (mentioned below) there are also some cases where the player should deviate from the basic strategy and play more or less aggressively based on the count.

### Hi-Lo system

There are many different counting systems, but they all work by assigning point values to cards.

- As the player sees cards, he keeps a count of their cumulative point score
- This score tracks what has been dealt so far, and therefore summarizes whether the remaining cards in the deck are favorable or unfavorable
- Based on the point total, the player adjusts his bets up or down, to take advantage when the deck is favorable and minimize losses when it isn't

The most recommended card counting system for blackjack is the [Hi-Lo system](https://wizardofodds.com/games/blackjack/card-counting/high-low/). It assigns points to the cards as follows:

- Cards 2-6 are worth +1 points
- Cards 7-9 are worth 0 points
- Cards 10, J, Q, K, and A are worth -1 points

#### The running count

As the player sees cards, he maintains the *running count* of their cumulative points. For example, suppose the player is starting a new game with a fresh deck. The running total is initially 0. On the first hand, the following cards are dealt:
```
Player: J 8 (stand with 18)
Dealer: 2 4 Q 6 (bust with 22)
```
The running total is updated to +1. Notice that positive scores are favorable to the player and negative scores are unfavorable.

#### The true count

Some Vegas casinos still offer single-deck blackjack, but it's more common to play out of a *shoe* of six or eight decks shuffled together. When dealing out of a shoe, the count needs to adjust for the number of remaining cards. Intuitively, a count of +5 is amazing for the player in a single deck, but not as impressive if there are still six decks of cards to work through.

The *true count* is calculated as
```
true_count = round(running_count / number_of_remaining_decks)
```
For example, if the running count is currently +6 and there are about 3 decks remaining, the true count would be +2.

#### Adjusting bets and strategy

The last step is to adjust the bet amount based on the true count. As the count goes higher, the player should bet more. In the real world, this has to be done subtly, to avoid attracting heat from casino managers who are suspicious of suddenly aggressive bets.

There are also some strategic plays that change based on the count. When the count is positive, there are more tens and aces:

- Blackjacks are more common, for both the player and the dealer. This is overall helpful to the player, since a win on a blackjack pays 3:2.
- The insurance side bet, if it's offered, has a positive expected value when the count is high enough
- The dealer is required to hit on scores of 12-16 and is therefore more likely to bust in a ten-rich deck. This creates some situations where it's better for the player to stand when the basic strategy says to hit.

## Implementation

### Objective
Extend the basic version to evolve a card counting system and betting strategy. The player now tracks cards as they are dealt from a multi-deck shoe and adjusts bet sizes based on the count.

### Game Rules
The following rules replace or extend the basic version:

- Hands are dealt from a 6-deck shoe (312 cards)
- Each fitness evaluation begins with a freshly shuffled shoe
- Cards are dealt from the shoe until reaching 75% penetration (234 cards dealt)
- When penetration is reached, the dealer completes the current hand, then reshuffles to begin a new shoe
- The player has a starting bankroll of $1,000
- Minimum bet is $1; maximum bet is $8
- Blackjacks pay 3:2 (e.g., a $2 bet wins $3 on a natural 21)
- If the player's bankroll reaches $0, the round ends immediately

### Strategy encoding

The chromosome now consists of three components.

**Component 1: Play strategy (260 bits)**. Identical to the basic version—a 17×10 hard hands matrix plus a 9×10 soft hands matrix encoding hit/stand decisions.

**Component 2: Card count values (22 bits)**. For each card rank, encode a count value from the set {−1, 0, +1} using 2 bits:
```
 Encoding |  Value
-------------------
    00    |    -1
    01    |     0
    10    |    +1
    11    |   unused (treat as 0)
```
Encode count values for 11 card values: Ace, 2, 3, 4, 5, 6, 7, 8, 9, and 10. All ten-valued cards use the same count value.


**Component 3: Bet multipliers (12 bits)**. Encode a bet multiplier (1–8) for each of four true count ranges. Each multiplier requires 3 bits:
```
 True count range |  Bits
--------------------------
      <= -2       |  3 (values 0-7 map to multipliers 1-8)
    -1 to +1      |  3
    +2 to +4      |  3
      >= +5       |  3
```

### Counts

The running count is maintained by adding the encoded count value for each card as it is revealed (player cards, dealer cards, and any other visible cards).

The true count normalizes the running count by the number of decks remaining:
```
decks_remaining = remaining_cards / 52
true_count = round(running_count / decks_remaining)
```
For example, with 156 cards remaining (3 decks) and a running count of +6:
```
true_count = round(6 / 3) = +2
```

### Bet sizing
At the start of each hand, the player determines the bet as follows:

- Calculate the true count
- Look up the bet multiplier for the corresponding true count range
- `bet = multiplier × $1`

The bet is capped at the player's current bankroll (i.e., the player cannot bet more than they have).

### Fitness Function
Fitness is the player's final bankroll after playing 1000 simulated hands. If the player's bankroll reaches $0 before completing 1000 hands, fitness is 0.

## Outputs

- The fitness plot and strategy heat map, as in the first project
- Evolved count values for each card rank and their comparison to the hi-lo system
- Display the evolved bet multipliers for each true count range as a table
- For the best-performing individual in the final generation, plot bankroll over the course of a sample 1,000-hand session. This helps visualize variance and the effect of bet sizing.
