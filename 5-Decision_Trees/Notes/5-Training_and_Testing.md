# Validation: Precision vs. Recall

## Overview

We've been focusing so far on the mechanics of training models: decision trees, entropy, random forests, and so forth. We'll now turn our attention to the second step in the process: evaluating the quality of a trained model.

This note will focus on the mechanics of training, testing, and validation. In particular, we'll focus on how to ensure that a model learns to *generalize* beyond its training data.

## Training and testing sets

In the first model of the practice lab, we trained a decision tree on *the entire Titanic data set*. As we said back then, this is dumb: given enough time and parameters, any model can achieve perfect classification of its training data by just memorizing the answers. This leads to the problem of **overfitting**, where the model performs well on its training data, but doesn't generalize to previously-unseen data.

Therefore, training a real model requires holding back some of the data as the **testing set**, which is used as an evaluation after training to score the model's performance. Reserving 20% of the data for testing is a common guideline.

### Train, validate, test

The basic idea of model testing is straightforward, but it's surprisingly easy to mess up and accidentally incorporate information from the test set into model training.

Training often requires making decisions about **hyperparameters**, the higher-level settings of the algorithm that guide the training process. For example, setting the maximum depths and leaf size in a decision tree, or the choice of information gain vs. Gini impurity as a splitting heuristic.

A common error is to train a model, test it, then adjust the hyperparameters and retrain the model to maximize performance on the test set. This loop indirectly makes the test set part of the training process!

A **validation set** is another chunk of the data that's separate from both the training and test sets. The training set is used to train the model and the validation set is used in a loop to adjust the parameters and architecture of the training algorithm. Then, after the final model is trained, the test set is used *one time* as an overall evaluation of its performance.

### Pre-processing

Another subtle issue involves pre-processing data before training. It's common to do data transformations or statistical operations like normalization before training a model.

Suppose that you first normalize your data, *then* split it into training and testing sets. The normalization operation included the testing data, so its statistical information has been accidentally incorporated into the training set. This is called *data leakage*.

Always split the data first, then perform data transformations on the individual sets, using only their specific values.

## Cross-validation

One limitation of the standard train-test approach (with or without a separate validation set) is that it only offers one estimate of the model's performance. It would be nice to have multiple independent testing sets to reduce the probability that we get a good test result by random chance, but this is usually impractical.

***K*-fold cross-validation** is a method for obtaining more testing observations from a limited amount of data.

- Randomly shuffle the data, then divide it into *k* equal-sized subsets, called *folds*.

- Set the first fold aside as a testing set, then train a model on the remaining *k* - 1 folds. Test on the first fold and record the result.

- Repeat the process with the second fold as the test set, then the third fold, and so forth. Each iteration trains a new model on *k* - 1 folds and tests on the remaining fold.

- Report the mean and variance of the *k* test estimates as the overall evaluations of model performance

5 and 10 are common values for *k* in practice.

Note that the splitting happens one time at the beginning of the method. Each data point is assigned to one fold at the beginning of the process, so each point is used 1 time for testing and *k* - 1 times for training. To avoid data leakage, transformations and preparations should only happen on each training subset, never on the entire data set.

In some cases, the splitting process needs careful attention. For example, if your data comes from repeated observations on individuals, you might need to make sure that all data belonging to a particular individual ends up in the same fold.

### Leave-one-out cross-validation

LOOCV is the extreme case of *k*-fold, where each data point is treated as its own fold. Each iteration trains the model on *n* - 1 data points and then tests on the single left-out point.

LOOCV lets every point be used for testing, so it gives an unbiased estimate of performance across the entire data set. However, if the number of points is large or models are time-consuming to train, it's probably impractical. It's most commonly used when the number of data points is small and you need to get maximum utility out of each one.
