# Decision Trees and Intro to Machine Learning

<img src="https://imgs.xkcd.com/comics/tasks.png" width="200px" />

*This was true in 2014.*


## Deliverables due and in-class quiz on 4/3


## Overview

We've talked about the general concept of machine learning before. A typical application is building a model that can learn, by observing a set of training examples, how to distinguish between classes of interest, with the goal of then classifying new observations that aren't part of the original training set. Image classification is an important practical example that was considered quite hard until it was solved by deep neural networks in the mid-2010s (more on those later).

Learning algorithms fall into two broad categories:

- *Supervised learning*, where the input data set consists of labeled training examples, and the goal is to learn a model that maps new previously unseen inputs to labels

- *Unsupervised learning*, where the input data set is unlabeled, and the goal is to learn a model that captures the structure of the data and reveals insights about meaningful subgroups. Clustering algorithms are an important category of unsupervised learning methods.

We're going to start our overview of ML by looking at one of the most important practical classification algorithms: the **decision tree**. Most of the work isn't in understanding decision trees themselves, which are straightforward, but in discussing how the algorithm chooses the decision splits at each branch. A second important topic is evaluating the quality of a machine learning model.

## Topics

- Structure of decision trees
- Entropy and an intro to information theory
- Using entropy to choose decision tree splits
- The GINI coefficient as an alternative split criterion
- Train-test splits
- Model valdiation: trade-offs between false positives and false negatives
- Precision and recall
- ROC curves
- Cross-validation

## Resources
