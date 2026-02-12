# Card Counting Strategy

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

Some Vegas casinos still offer single-deck blackjack, but it's more common to play out of a *shoe* of six or eight decks shuffled together.

When dealing out of a shoe, the count needs to adjust for the number of remaining cards. Intuitively, a count of +5 is amazing for the player in a single deck, but not as impressive if there are still six decks of cards to work through.

The *true count* is calculated as
```
true_count = round(running_count / number_of_remaining_decks)
```
For example, if the running count is currently +6 and there are about 3 decks remaining, the true count would be +2.

#### Adjusting bets and strategy

The last step is to adjust the bet amount based on the true count. As the count goes higher, the player should bet more. In the real world, this has to be done subtly, to avoid attracting heat from casino managers who are suspicious of suddenly aggressive bets.

There are also some strategic plays that change based on the count. If there are more tens and aces:

- Blackjacks are more common, for both the player and the dealer. This is overall helpful to the player, since a win on a blackjack pays 3:2.

- The insurance side bet, if it's offered, has a positive expected value when the count is high enough

- The dealer is required to hit on scores of 12-16 and is therefore more likely to bust in a ten-rich deck. This creates some situations where the player should stand when the basic strategy says to hit.

