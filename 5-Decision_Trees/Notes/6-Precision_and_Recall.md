# Precision and Recall

## Overview

Consider the following situation: you're building a model to predict the incidence of a certain rare disease. Your testing set consists of 2000 points, of which 10 are positive. Your model predicts negative for 1999 patients and correctly classifies 1 positive case, achieving 99.55% accuracy on the testing set.

Good job?

Clearly, we should be suspicious of this evaluation. The *accuracy*, the percentage of correct classifications, is high, but that isn't the right measurement here, because we've failed at the actual medically-useful task of identifying positive cases. An effective evaluation needs to measure how well the model does at *making useful predictions* even if one class is rare.

Rather than accuracy, model evaluations use two metrics called **precision** and **recall**.

## Precision

Think about a classification problem as a labeling task, where the model labels each item as "positive" or "negative". For example, in the *Titanic* data, we could think of "Did not survive" as being the "positive" class that we want to identify.

**Precision** is the fraction of correct positive classifications out all items labeled as positive.

- Suppose that a *Titanic* model labeled 100 passengers as "Did not survive", and that label was correct for 90 of them. The precision in that case would be 90 / 100 = 90%.

- In the medical testing example above, we classified 1 patient as positive and that was correct, so the precision is 100%.

```
                 correct positive classifications
Precision =  ----------------------------------------
              correct positves + incorrect positives
```
Or, using different names:
```
                       true positives
Precision =  ---------------------------------
              true positives + false positives
```

I like to think of a high-precision model as *trustworthy*. When it says an item is positive, it is very likely to be correct. The predictions of a low-precision model would be untrustworthy.

"*But wait*!" you say. "*Precision can be high even if the model fails to recognize positive cases*." 

That's exactly right. The precision formula only penalizes for incorrect positive classifications. There is no penalty for *false negatives*, where the model should have returned a positive label but gave a negative one. Therefore, precision incentivizes conservatism - don't label an item as positive unless you're very sure that's correct.



## Recall

**Recall** is the fraction of true positive classifications out of all items that *should have been classified as positive**.

```
                  true positives
Recall = -------------------------------- 
         true positives + false negatives
```

In our medical example, the model found 1 correct positive and 9 false negatives, so its recall would be only 10%.

A model with high recall is *thorough*: it is likely to find all positive cases. Notice that false positives are not part of the recall calculation, so one way to achieve a high recall is to label *everything* as positive.


## Library example

Imagine that it's 1992 and you're ten years old and in the fifth grade and have to do a research paper on frogs. You won't know about the Internet until next year, when you go over to your friend Patrick's house and he has a Mac and the Prodigy online service, so you have to look for real books on frogs in your school library. Let's imagine that the library has 2500 total books, of which 30 are about frogs. The library does have a computer you can use to search (it's the 1990s, not the Stone Age). It's helpful to think about the extremes of precision and recall in terms of real numbers:

- A search with high precision and high recall (the ideal case) would return the 30 frog books and nothing else

- A search with high precision but low recall would return just 1 frog book and nothing else

- A search with high recall but low precision would return all 2500 books in the library

- A search with zero precision and recall (the worst case) would return all 2490 books *not* about frogs. This search returns the exact opposite of what it should.

What if the search returned 50 results, of which 25 were frog books? In that case:

- The precision is 25 / 50 = 50%
- The recall is 25 / 30 = 83%

What if we just selected a random collection of *n* books without worrying whether they're correct or not? In that case,

- We'd expect 30/2500 = 1.2% of books we select to be about frogs, so the expected precision is always 1.2%.
- The recall scales with *n*. If we take 250 books, we've taken 10% of the library, so we'd expect to get 10% of the frog books on average

A minimal baseline of model performance is doing better than random.

## F1 score

The F1 score combines precision and recall into one value in the range of 0 to 1. It therefore provides a single score of model performance. The F1 formula is:

$$ F_1 = \frac{2}{precision^{-1} + recall^{-1}} = 2\frac{precision \cdot recall}{precision + recall} $$
