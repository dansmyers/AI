# Evolving Blackjack Strategy

[I also like to live dangerously.](https://www.youtube.com/watch?v=JVwEf7xSjwY)

## Overview

*Blackjack*, sometimes known as 21, is the most popular table game played in American casinos. The object is to obtain a hand of cards that scores higher than the dealer's hand without going over a score of 21.

In this project, you're going to use genetic programming to **evolve a strategy for blackjack**. Your strategy will specify under what circumstances the player should hit or stand. You'll score the fitness of each strategy by playing simulated hands of blackjack, then use the genetic algorithm technique to evolve new strategies that descend from the current top performers. The overall goal is to evolve a strategy that performs close to the theoretically optimal win rate of approximately 49.5%.

## Disclaimer

These projects are for educational purposes only. They are not an endorsement of the extremely cool vice of gambling.

## Rules

If the rules of blackjack aren't familiar to you, first spend some time learning the game. I recommend the [rules summary](https://wizardofodds.com/games/blackjack/basics/) from the Wizard of Odds, my go-to source for gaming knowledge. You can find a free practice game online, or just ask Claude to code one for you.

Our version will only allow the player to **hit or stand**. We won't consider alternative moves like doubling, splitting or surrendering, or side best like insurance. This means that at every decision in the game is a binary choice to either hit or stand.

For this project, we're going to focus on *single-deck blackjack*, which is generally more favorable to the player. Most Vegas casinos now play -with 6 or 8 decks shuffled togehter to reduce the impact of card counting (more on that in the next project).

## Basic strategy

<img src="https://wizardofodds.com/blackjack/images/bj_1d_s17.gif" width="300px" />

The Wizard's basic blackjack strategy is given in the table above. Observe that each entry corresponds to a player hand value and the dealer's face-up card. For example, if the player has a hand value of 12, he should hit if the dealer shows a 2 or 3, stand if the dealer has a 4-6, and hit on all higher-valued cards.

The second table is for "soft" hands where the player has an 11-valued Ace. These can be played more aggressively, since it isn't possible to bust by hitting a soft hand - if the player draws a card that would make the score greater than 21, then the value of the Ace changes to 1. The tables specify cases where the player should double if allowed; we're not implementing doubling, so these should revert to the basic hit/stand choices.

The third table is for paired hands. Many casinos allow the player to "split" pairs, doubling the bet to play two hands. We're not implementing splitting, so ignore this table.
