# The Multi-Armed Bandit

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Liberty_bell.jpg" width="300px" />

*Charles Fey's "Liberty Bell" slot machine, ca. 1899. An immigrant to San Francisco from Bavaria, Fey invented the classic slot machine with three rotating reels of symbols in about 1890. Some prototype gambling machines already existed, but Fey's was the first to fully automate the payout mechanism and become a huge success. The classic version had five symbols on each reel, one of which was the Liberty Bell that gave the machine its name. Via Wikipedia.*


## Overview

In the old days, slot machines were known as "one-armed bandits", after the classic design with a big lever the player pulls to activate the spinning reels.

The **multi-armed bandit** is a problem in decision theory inspired by the slot machine concept.

- Suppose that we have a setup of *K* slot machines. Each machine has its own unique reward distrbution, but we don't know the distributions for any of the machines.

- We're allowed to make *T* free pulls, choosing one machine each time to activate

- Each pull gives a random reward from its chosen machine according to that machine's distribution, which again, we don't know

**How should you distribute your pulls to get the maximum expected reward**?

This model turns out to be relevant to problems that involve trading off *exploration* vs. *exploitation*. At the beginning of the game you know nothing about any of the payout distributions for any of the machines. As you make pulls, you earn rewards, which allow you to infer information about their machines' hidden distributions. So you have a trade-off between spending pulls to learn more about the payout behavior of the different machines vs. concentrating your pulls on the machine that seems to give the best reward.

The *explore vs. exploit* dynamic was also present in our local search algorithms, where there was a tradeoff between using methods like hill-climbing to aggressively ascend to the immediate local maximum vs. spending time moving around the search space with the intent of finding an overall better maximum.

## Regret

Let $$\mu_k$$ be the mean reward of machine $$k$$. Let the maximum reward be

$$ \mu* = \max_k \{ \mu_k \} $$
