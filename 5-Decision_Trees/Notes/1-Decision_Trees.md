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


## Boosting
