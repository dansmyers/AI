# Bayesian Spam Filtering

## Due 4/24

## Overview

We've seen a few different classification approaches so far in this class:

- Decision trees performed classification by successively splitting data into purer subsets
- The linear perceptron found a separating hyperplane
- The multilayer perceptron learned a nonlinear separating boundary, which might be arbitrarily complex

There is another major approach that we haven't discussed yet: treating classification as a **probability problem**. The most important algorithm in this category is the _Bayesian classifier_, which formulates the classification problem as a conditional probability using Bayes' Rule. The standard implementation is often called the _naïve_ Bayesian classifier, because it makes some simplifying independnece assumptions, which we'll discuss more later. These assumptions are ad-hoc, but turn out to work well for many real world problems.

An important practical application of the Bayesian classifier is **e-mail spam filtering**. The rest of this write-up will work through the details of the spam filtering problem. By the end of this project you will be familiar with:

- Formulating a classification model as a conditional probability problem
- Using Bayes' Rule to derive an expression that can be used for making predictions
- How the naïve Bayesian classifier works
- How to use naïve Bayes to classify texts


## Bayesian Classification

<img src="https://imgs.xkcd.com/comics/machine_learning_2x.png" width="33%" />

### Classification as a Conditional Probability

The Bayesian approach considers classification as a **probability problem**.

Intuitively, there are some words that are likely to occur in spam message but not in legitimate messages. Suppose we have the text of an input message *m*. We'd like to use the *words* in *m* as our features to determine if *m* is spam or not. We could, potentially, expand the model to consider features other than just the contents of the message, but we won't worry about that in these examples.

Consider two conditional probabilities:

```
P(m is spam | words in m)
```
```
P(m is NOT spam | words in m)
```
If we could calculate these two probabilities for the message *m*, then we can assign *m* the class that has the higher probability.

Here's the problem: **how do we calculate these two probabilities**? To begin, let's think about the reversed conditonal probability:
```
P(words in m | spam)
```
This probability expresses the likelihood that a message picked from the universe of all spam messages contains the words we observed in message *m*.

***We can estimate this from the training data***. That is, we can collect a training set of real spam messages, count the words they contain, and use that data to build a model of spam message vocabulary. We can then do the same thing for non-spam message 

### Intuition

If you're not sure about this part, consider a message that contains the words "**FREE HERBAL VIAGRA**".  I do not often receive legitimate messages on this topic,
so I'd expect `P("FREE HERBAL VIAGRA" | not spam)` to be very close to zero. The other case, `P("FREE HERBAL VIAGRA" | spam)`, should be much higher.

### Bayes' Rule

**This is the perfect setup for Bayes' Rule**. We have a conditional probability of interest that's hard to calculate directly, but we can reason about the reversed conditional probability.

But first, let's simplify the notation a little bit. Let *c* denote a class of interest, either *spam* or *not spam* in this example. Let *m* denote the contents of the
message.

Bayes' Rule states that:
$$ P(c | m) = \frac{P(m | c)P(c)}{P(m)} $$

- $$P(c | m)$$ is the classification probability, where *c* is a class of interest (either "spam" or "nor spam") and *m* is the text of the input message

- *P*(*m* | *c*) is the reversed conditional probability which we interpret as the probability of observing message *m* if it really belongs
to class *c*. Most of the model's work is calculating this quantity, which we'll discuss below. This probability is also called the **likelihood**.

- *P*(*c*) is the **unconditional probability of observing class *c***, independent of any information about the message. If *c* is the class of spam messages, then this is the probability that an arbitrary message is spam. In Bayesian statistics, this is called the **prior**  probability. If you have reason to believe that one class is more likely than another, the prior probability allows you to incorporate this information into the model.  

  For example, suppose that we believe 80% of all e-mail traffic is spam and only 20% is legitimate, which is consistent with research estimates. Using these probabilities for *P*(spam) and *P*(not spam) would make it easier for us to classify messages as spam and require a higher likelihood to classify a message as non-spam.
as non-spam.  

  In practice, we could use pre-existing evidence to set these values or estimate them from the training set. Assuming that both classes are equally likely is also called a "flat prior".

- The denominator, *P*(*m*), is the unconditional probability of observing a message with contents *m*, across the universe of all spam and non-spam messages. Notice:
**this does not depend on *c***! Therefore, *P*(*m*) will be the same for both classes and we can ignore it in our calculations.

## Example

This is all pretty abstract, so let's look at how this plays out in a **small** example.

Suppose we have a universe of only four messages, two spam and two non-spam. Let's assume the messages have been pre-processed to remove all punctuation and case.

| Message contents           | Class label |
| -------------------------- | ----------- |
| watch free anime downloads | spam        |
| see you at the house       | not spam    |
| do you want takeout        | not spam    |
| sell your house now        | spam        |

Question: Is the message "you want to watch anime at my house" more likely to be spam or not spam? Using the Bayesian formulation, we need to calculate two probabilities:
```
P(spam | "you want to watch anime at my house")
```
```
P(not spam | "you want to watch anime at my house")
```
Once we've performed both calculations, we'll take the larger probability to be the correct classification. From the previous section, we want to calculate the numerator of Bayes' Rule:
```
P(spam | "you want to watch anime at my house") = P("you want to watch anime at my house" | spam) P(spam)
```
And likewise for the "not spam" class.

### Prior Probabilities

First, let's consider the prior probabilities. Because we have an equal number of training examples in each class, we could reasonably decide that
```
P(spam) = P(not spam)
```
which means that the priors will not affect our classification decision, and can be dropped from further calculation. If we felt it was important to weight one class as more likely than the other, we could change the prior probabilities to do so.

### The Naïve Bayes Model

We now need to consider the likelihood of the message conditioned on each class, and to do it we're going to make a very strong simplification: **Assume that every word in a message is independent of all of the other words**. This is a strong assumption! By assuming independence, we're choosing to ignore all word context, sentence  structure, grammar, and any other aspect of language that makes some words more likely to appear together.

If all of the words are independent, then the likelihood of the entire message is the product of the individual word likelihoods

```
P("you want to watch anime at my house" | spam) = P("you" | spam) * P("want" | spam) * P("to" | spam) * ... * P("house" | spam)
```

A Bayesian model that assumes independence of the features is called a **naïve Bayesian classifier**, because the assumption of independence is almost always technically wrong. Despite this, naïve Bayes actually works well for real-world problems including text classification, so it's a standard technique in the field.

### Estimating Word Likelihoods

Estimating the likelihood of individual words is easy:
```
                  Number of times word occurs in all spam messages
P(word | spam) = --------------------------------------------------
                      Count of all words in all spam messages
``` 
For example, the word "anime" occurs one time in the set of spam messages and there are a total count of eight distinct words in the entire spam data set, so we estimate
```
P("anime" | spam) = 1 / 8 = .125
```
This is equivalent to saying that 12.5% of all words in spam message should be "anime".

### Removing common words

There are two issues to consider before moving on the final calculations.

First, some words &ndash; "a", "at", "the", "to", etc. &ndash; are so common they won't yield useful classification information. We can ignore these. More generally, we could pre-filter all messages to focus on only a subset of key words that we think are useful for classification. This has the advantage of making our feature vectors smaller and reducing irrelevant information in the model, at the risk that we choose to exclude something that would actually be useful.

The non-spam set contains "at" and "the". If we remove those, there are *6* distinct words: "see", "you", "house", "do", "want", "takeout".

### Smoothing

The second issue is more complicated. What about words that don't appear in one of the data sets? For example, "anime" does not appear in the non-spam data set, but we don't want to automatically conclude that `P("anime" | non-spam) = 0`, because that would mean that "anime" can't occur in non-spam messages.

A typical solution to this problem is to assume that every word has some small constant probability of occurring, even if it was never observed in the training data set. Modify the word likelihood formula to be
```
                                  Number of times word occurs in all spam messages + 1
P(word | spam) = ---------------------------------------------------------------------------------------
                      Count of all words in all spam messages + Number of unique words in all messages

```
The numerator is now guaranteed to be at least 1, even a word does not appear in any messages. To compensate for this change, the denominator has been increased to
include the number of unique words in all messages (the **vocabulary** of the training set). Our training set contains 13 unique words after dropping "at", "the", and "do".

Under these new assumptions, we can calculate

```
                      1 + 1
P("anime" | spam) =  -------- ~ .095
                      8 + 13
```

The corresponding non-spam probability is

```
                           0 + 1
P("anime" | not spam) =  -------- ~ .053
                           6 + 13
```
The fancy name for this adjustment is **Laplace smoothing**.

### Results

Here is the table of likelihoods for the important words in "you want to watch anime at my house" calculated using the Laplace smoothing strategy.


| word | P(word \| spam)  | P(word \| not spam) |
|------| ----------------- | ------------------- |
| you | .0476 | .158 |
| want | .0476 | .105 |
| watch | .095 | .053 |
| anime | .095 | .053 |
| my | .0476 | .053 |
| house | .095 | .105 |

For example, "you" appears two times in the non-spam messages and zero times in the spam messages. It's probabilities are therefore:
```
P("you" | non-spam) = (2 + 1) / (6 + 13) ~ .158
```
```
P("you" | spam) = (0 + 1) / (8 + 13) ~ .0476
```

Also observe that "my" doesn't appear in either the spam or non-spam group of training examples, but we can still calculate non-zero probabilities for it because
of smoothing.

### Finally

The final step is to calculate the likelihood of the entire message "you want to watch anime at my house". The naïve classifier assumes independence, so the overall likelihood is the product of the word likelihoods:
```
P("you want to watch anime at my house" | spam) = P("you" | spam) * ... * P("house" | spam)

                                                = .0476 * .0476 * .095 * .095 * .0476 * .095
                                              
                                                = 9.247e-8
```
The corresponding probability for the non-spam case is

```
P("you want to watch anime at my house" | not spam) = .158 * .105 * .053 * .053 * .053 * .105
                                           
                                                    = 2.593e-7

```

Based on these results, we conclude that "you want to watch anime at my house" is **most likely not spam** because the non-spam case yields the higher value.

Note that this numbers aren't really probabilities, because we dropped the denominator from the Bayes' Rule calculations. The results are still **proportional** to the true probabilities, which is what allows us to conclude that the not spam case is more likely.

## Practice Problems

Using the training data set given above and the naïve Bayesian classifer technique, determine whether the following messages are more likely to be spam or not spam.

1. "watch anime now"

2. "takeout and anime at my house"

3. "sell me your anime collection"

## Summary

All of the challenge in this project is in working through the details of the naïve Bayes model. You should be able to complete the calculations and scikit-learn example
without difficulty if you understand the model.

This example is just scratching the surface of machine learning in general and statistical learning in particular. If you're interested in learning more, I recommend starting with [this video](https://www.youtube.com/watch?v=aircAruvnKk&vl=en) on neural networks and the handwritten digit classification problem.
