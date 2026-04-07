# DIY Backpropagation

### UNDER CONSTRUCTION - DON'T START ON THIS YET

## Overview

It's time: implement your own version of the backpropagation algorithm that can train a neural network with one hidden layer and an arbitrary number of nodes.

You're going to write two scripts:

- One that trains a model to learn the basic XOR function. Recall that this was one of the functions that isn't lineraly separable.
- A second one that trains on the iris data set from the last unit. This demonstrates creating a network with three output nodes.

One request: for this problem, it's okay to use **AI chat** to help you, but don't use Claude Code to generate all of the code in one shot. I would like you to spend a little time working through the details of the backpropagation algorithm.

## Basic Strategy

Your implementation is going to represent a multilayer perceptron with an input layer, a _single hidden layer_ that has an arbitrary number of nodes, and the output layer.

You should implement the following functions:

- `sigmoid(x)`: calculate the sigmoid value of input `x`. Used by both the `predict` and `train` functions.

- `predict(hidden_weights, output_weights, point)`: classify the input point using the given input-to-hidden-layer weight matrix and the given hidden-to-output-layer weights. The structure of the weight inputs are discussed below.

- `train(hidden_weights, output_weights, point, target_label, learning_rate)`: perform a classification step and then a backpropagation update to all weights using the given point and target label.
 
- `epoch(hidden_weights, output_weights, training_set, training_labels)`: perform a complete training epoch on the given set of training points with their associated labels. Basically a loop that wraps around the `train` method.

- `evaluate(hidden_weights, output_weights, testing_set, testing_labels)`: predict the class (without performing any training) on the given set of test points and report the fraction that are classified correctly. This is the final function used to evaluate the performance of the training network.

Most of the work is in the `train` method. The other methods are really wrappers around the training process. Therefore, you'll need to think about how to implement the backpropagation calculations.

You can add other methods or structures if they're helpful.

### Weight representation

The first set of weights connects the input layer to the hidden layer. Suppose the input dimension is *n* (that is, the inputs are *x*<sub>1</sub> to *x*<sub>*n*</sub>) and there are *h* neurons in the hidden layer.

Including the biases, there are (*n* + 1)*h* total weights in this set. It's convenient to think about these weights as a matrix:

```
[ w_10   w_11   w_12   w_13  ...  w_1n ] 
[ w_20   w_21   w_22   w_23  ...  w_2n ]
[                   .                  ]
[                   .                  ]
[                   .                  ]
[ w_h0   w_h1   w_h2   w_h3  ...  w_hn ]
```

The first row represents the weights for the first hidden node. The first element `w_10` is the bias for hidden node 1, the second `w_11` is the weight connecting input 1 to hidden layer 1, and so forth.

The other rows contain the weights for the other hidden layer nodes, with the last row representing node the last hidden node *h*.

The second set of weights connects the hidden layer to the output neuron. This is a vector of *h* + 1 weights, including the bias.

```
[ w_0   w_1  w_2  ...   w_h ]
```

### Parameters

- The initial values of all the weights and biases should be randomized to values in [-1, 1].

- **You must have a variable that controls the number of hidden-layer nodes and your code must work for any reasonable number of hidden-layer nodes**. You can't hard code the calculations for a specific number of hidden layer nodes; your method must be generalize for different numbers of weights.

- You only need to support one hidden layer

## Warm-Up: XOR

Train a network that can learn the XOR function:

```
x_1  x_2  |  x_1 XOR x_2
----------|-------------
 0    0   |       0
 0    1   |       1
 1    0   |       1
 1    1   |       0
```

Remember that this is one of the classic functions that isn't linearly separable. There is no separate test set for this problem.

## Fisher's Irises

### Overview

Modify your neural network implementation to learn a model that can classify the iris flowers. Copy the dataset from the previous projecy.

Create a test set by randomly selecting 30 items (20% of the total 150). The remaining 120 items will be the training set. Remember that the test set should only be used for the final evaluation of the model and can't be part of the training process. It's desirable to randomize the order of the training examples.

This question introduces a new challenge: there are *three classes*. Your network will have three output nodes, one for each class:

- Each node corresponds to one of the three flower classes.

- Each output node has **its own set of weights** connecting it to the hidden layer. The output-layer weights are now a 3 row by *h* + 1 column matrix, rather than a single *h* + 1 element vector.


### Multi-class outputs

The goal is to train the model so that each node outputs 1 when the input belongs to its class and 0 for inputs in other classes. For example, when presented with a point in class 1 (the `Iris-setosa` class), the first output node should be 1 and the other two should be 0. Suppose that the first training example is the first point in the dataset:

```
5.1,3.5,1.4,0.2,Iris-setosa
```
The correct response to this input is for the first output node to have value 1 and the other two to be 0. The other two classes are similar: the second node should be 1 for points in the `Iris-versicolor` class and the third should be 1 for points in the `Iris-virginica` class.

The weights of the network are initially random, so the output of the three nodes will be random values between 0 and 1. Suppose the network produces the following three output values:
```
output of node 1 = .36
output of node 2 = .79
output of node 3 = .12
```
Choose the highest output value as the overall classification, which is class 2 (*iris versicolor*) in this case.

If the input really belonged to class 1, the the errors are:
```
error_1  =  (1 - .36)   
error_2  =  (0 - .79)
error_3  =  (0 - .12)
```

The update rules remain the same. Remember: you already had to figure out how to update a matrix of weights for the hidden layer, so updating the output layer weights for a network with multiple output nodes is not that different.

### Output

**You don't need to achieve perfect classification**, but you should be able to demonstrate that your network is learning. Produce a plot showing the average training error at the end of each epoch and show that the error is decreasing over time.


## Variaion: ReLU activation

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/ReLU_and_GELU.svg/1920px-ReLU_and_GELU.svg.png" width="250px" />

*The ReLU function in blue. The GeLU function is a variation that adds nonlinearity to make the gradient nonzero when the input is negative. (via Wikipedia)*

The classic sigmoid activation function has a problem that shows up when trying to train larger networks: if the input is very large or very small, the output saturates at 0 or 1 and the gradient is tiny, which makes learning difficult.

An alternative is the **rectified linear unit** (ReLU), which simply outputs `max(0, x)`, as shown in the figure above. The ReLu function can also be written as:

$$ ReLU(x) = \frac{x + |x|}{2} $$

The "rectified" name comes from electronics, where a *rectifier* is a circuit element that converts AC current into DC by blocking the negative part of the alternating cycle. The term also shows up in audio engineering, where it's related to [amplifier distortion](https://www.gibson.com/products/mesa-boogie-90s-dual-rectifier?view=mesa) (🤘😈🤘).

- Do some research on why the ReLU function is preferred for training modern neural networks. Also look at the "leaky ReLU" variation and explain why it's sometimes preferable to the basic ReLU.

- Create a second version of your iris program that uses the ReLU at the *hidden* layer. Continue to use the sigmoid at the output layer, since the result you care about is a class label in [0, 1]. Compare the training error plot to the one produced by the sigmoid function. You can use Claude Code to help you with this part.

