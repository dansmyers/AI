# The Multi-Armed Bandit

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Liberty_bell.jpg" width="200px" />

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

Let $$\mu_k$$ be the mean reward of machine $$k$$. Let $$\mu^{*}$$ be the maximum of the means across the $$K$$ machines.

$$ \mu^{*} = \max_k \{ \mu_k \} $$

Therefore, over $$T$$ pulls, the maximum reward the player could expect to obtain is $$\mu^{*}T$$.

In practice, if the player pulls arm $$k$$ a total of $$T_k$$ times, then the expected reward from machine $$k$$ is $$\mu_kT_k$$. Let the *regret* be the difference between the max expected reward and what the player actually obtained:

$$ regret = \mu^{*}T - \sum_{k=1}^{K}  \mu_kT_k $$

The right term is the sum of rewards over all machines, taking into account the number of plays made on each machine.

The ideal solution would be a strategy that *minimizes regret* - but you can't really find that, because the true $$\mu_k$$ and $$\mu^{*}$$ are unknown. Instead, the prefered approach is to play a strategy that *bounds regret*.

## Upper Confidence Bound

The UCB strategy is the standard technique for playing the multi-armed bandit problem. It was introduced in a [2002 paper](https://link.springer.com/article/10.1023/A:1013689704352) by Peter Auer, Nicolò Cesa-Bianchi, and Paul Fischer.

The UCB strategy considers a situation where you can keep pulling as many times as you want. Each pull gives you some information about the behavior of its machine, and you would like to play in such a way that regret is minimized over the long run of play.

Suppose that we have played some number of pulls $$t$$. Let $$\overline{x_k}$$ be the average reward per pull obtained from machine $$k$$ over those pulls. That is, $$\overline{x_k}$$ is our estimate of what we earn for each pull of arm $$k$$.

Intuitively, picking the arm with maximum $$\overline{x_k}$$  is reasonable: you might as well play the arm that seems to be giving the highest rewards.

However, the more times we play $$k$$, the better we understand its reward distribution. An exploration strategy might assign more weight to arms that we haven't played as much yet, as a way to learn more about them.

The UCB strategy says that, on each pull, to play the arm $$k$$ that maximizes,

$$ x_k + \sqrt{\frac{2 \ln t}{t_k}} $$

where $$t$$ is the total number of pulls made so far and $$t_k$$ is the number of pulls of arm $$k$$.

The first term is the straightforward expected reward; the bigger it is, the more we expect to earn from arm $$k$$. The second term is the exploration adjustment. It gives more weight to arms that haven't been played much relative to the total number of pulls.

It turns out that this strategy, which is simple to implement, achieves a regret that grows only logarithmically over time.

