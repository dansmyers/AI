# Decision Trees

## Overview

Decision trees are a popular and conceptually simple classification algorithm. For us, they'll serve as our intro to the fundamental concepts of machine learning.

A decision tree is structured like a top-down flow chart. The internal nodes represent decisions based on the attributes of a data item; the leaves represent classifications. Given a new item that needs to be classified, start at the top and work your way down, taking the appropriate branch at each internal node, until you reach a leaf. Then assign the item the class corresponding to the leaf.

Decision trees are *non-parametric* models, in that they don't require any assumptions about the underlying statistical behavior of their data. They're also easy to visualize and understand.

On the other hand, the performance of a decision tree depends  heavily on its depth, which is hard to determine _a priori_. The simplest implementations are prone to overfitting their training data.

## Method

The canonical decision tree algorithm is **CART** ("Classification and Regression Trees"), which is the default method in `scikit-learn` and was first introduced in 1984. Two other common decision tree algorithms are ID3 ("iterative dichotomiser version 3") and C4.5, both developed by Ross Quinlan in the 1980s. The different methods differ in some of their details, but have the same general approach.

The decision tree method starts by creating a root node that represents all of the training data. It then selects a feature to use as a split condition, creating two child nodes that subdivide that data set. The method then repeats recursively on each child: choose another split feature and divide into more children. This process continues until the method succeeds in carving out leaves that contain examples of only one class, or a pre-set stopping depth is reached.

Most of the work is in choosing the best split. This is done by considering each feature and then choosing the split that does the best job of separating the current node's data into distinct classes. CART uses the Gini impurity measure for this calculation; C4.5 uses entropy and information gain. Both are discussed in the next notes.

## Pseudocode

The example method implements the vanilla decision tree algorithm. It uses an `information_gain` function (not shown) to score the quality of each split.

```
Basic Decision Tree

split(data, depth) {
    // Base case - depth limit
    if depth > MAX_DEPTH {
        return LeafNode(class: majority(data))
    }

    // Base case - data size less than threshold
    if size(data) < MIN_DATA_LENGTH {
        return LeafNode(class: majority(data))
    }

    // Base case - pure leaf
    if all data items have the same class {
        return LeafNode(class: data[0].class)
    }

    // Choose the best feature
    max_gain = -infinity
    best_feature = null
    best_value = null

    for each feature of data {

        // Consider all possible splits for that feature
        for each value of feature {
            // Binary split based on candidate value
            left = {data with feature <= value}
            right = {data with feature > value}

            // Skip splits that put everything into one side
            if size(left) == 0 or size(right) == 0 {
                continue
            }

            // Score split
            gain = information_gain(data, left, right)

            if gain > max_gain {
                max_gain = gain
                best_feature = feature
                best_value = value
            }
        }
    }

    // Recursively split the best left and right subsets
    left = {data with best_feature <= best_value}
    right = {data with best_feature > best_value}

    left_child = split(left, depth + 1)
    right_child = split(right, depth + 1)

    // Return an internal decision node
    node = InternalNode()
    node.split_feature = best_feature
    node.split_value = best_value
    node.left = left_child
    node.right = right_child

    return node
}
```

Observe that the method always chooses a binary split. This is the approach used in CART, but isn't universal. ID3 and other methods allow multi-way splits in some cases.

During the feature-selecting loop, the method tests every value as a potential split. This is fine for features that are binary or have only a few choices, but would be cumbersome for integer- or float-valued features, or categorical features that have a many distinct values. Variations are:

- Sort the list of values, then consider them from smallest to largest. This allows you to update the information gain incrementally by only considering the number of items that move from the right set to the left set as the value increases

- Group the values into a pre-set number of histogram bins (say, 64) and use the bin boundaries as the candidate splits. This takes into account distribution information but reduces the number of choices down to a relatively small fixed size.

- Sample and score a random subset of values

## Pruning

If you completed the Titanic practice activity, you're familiar with the problem of **overfitting**, where a model achieves a high accuracy on its training data but doesn't generalize well to new data.

Setting the max depth of the tree is tricky. Basic implementations tend to build out trees with too many leaves, but stopping the building process early may hurt performance because a "bad" split early in the tree might enable a useful one later. A better option, used by the CART algorithm, is to first build out the tree, then *prune* unnecessary nodes. The goal of the pruning process is to trade off the size of the tree against classification performance and remove nodes to obtain a smaller tree that still performs reasonably well.

After building the complete tree, CART considers each subtree and evaluates the impact of collapsing it to a single leaf node. Pruning a subtree removes some leaf nodes, which hurts classification performance, but reduces the size of the tree. The key metric is the change in performance *per leaf node removed*. The best subtree to prune is the one that minimizes this metric: that's the subtree that offers the minimum impact relative to the number of nodes it contains.

The process then repeats, identifying a second subtree to prune, then a third, and so forth. The result of this process is a sequence of progressively smaller trees. The final step uses cross-validation (discussed in a future note) to select which tree in the pruning sequence offers the best cost-complexity tradeoff.


## Random Forests

If one decision tree is good, how about a *forest* of trees?

An **ensemble method** is a machine learning technique that trains a collection of models and lets them vote on the best classification. Typically the individual models are small and fast, and trained so that the weaknesses of some models are balanced by the strengths of others. Many of the top-performing systems on real-world classification problems are ensembles.

Some ensemble methods mix models of different types, but a common approach is to train multiple copies of the same model with randomized variations. The random forests technique trains a collection of small decision trees:

- Each tree is built from a sample of the overall training set. This is done by sampling *with replacement* to create a randomized training set the same size as the original set. This method is called [*bootstrap sampling*](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)).

- Each tree is also restricted to using a randomized subset of features, which forces the different trees to learn different classification strategies


The result is a collection of decision trees (each trained on a random sample of the training data and a randomized sample of features). A standard implementation may train dozens to hundreds of randomized trees. The trees are independent, so training and classification are easy to parallelize.

When it's time to classify a new input, each tree performs its own classification, then the majority label is assigned as the overall output.




