# DIY Backpropagation

## Due April 17

## You can work with a partner to complete this project

## Overview

This project is an extension of Assignment 4. You're going to build a feed-forward MLP model that can train on an arbitrary dataset with any number of hidden or output layer nodes.

## Methods

Write a script called `backpropagation.py` that contains the following methods:

- `sigmoid(x)`: calculate the sigmoid activation function for input `x`. Used by both the `predict` and `train` functions.

- `predict(hidden_weights, output_weights, point)`: classify the input point using the given input-to-hidden-layer weight matrix and the given hidden-to-output-layer weights. We'll discuss the structure of the weight inputs below.

- `train(hidden_weights, output_weights, point, target_label, learning_rate)`: perform a classification step and then a backpropagation update to all weights using the given point and target label. This is the main training function. You don't need to implement any batching.

- `epoch(hidden_weights, output_weights, training_set, training_labels)`: perform a complete training epoch on the given set of training points with their associated labels. Basically a loop that wraps around the `train` method and calls it for each point in the training data set.

- `evaluate(hidden_weights, output_weights, testing_set, testing_labels)`: predict the class (without performing any training) on the given set of test points and report the fraction that are classified correctly. This is the final function used to evaluate the performance of the training network.

You can add other methods or structures as you see fit.

## Weights

Suppose your network has *N* inputs labeled *x<sub>1</sub>* to *x<sub>n</sub>*. Each hidden layer node has a set of weights connecting it to all *N* inputs, which can be represented as a Python list. For example, if we're considering hidden node 1, its weight vector contains the entries

[*w<sub>10</sub>*, *w<sub>11</sub>*, *w<sub>12</sub>*, ... , *w<sub>1n</sub>* ]

Notice that the first weight is *w<sub>10</sub>*: this is the bias weight for hidden neuron 1. It's always paired up with an implicit input value of *x<sub>0</sub>* = 1.

Each of the *H* hidden layer neurons has its own vector of *N* + 1 weights for the *N* inputs plus the single bias weight. All of these weights together can be arranged into a *H* row by *N + 1* column list of lists representing the matrix of all weights for the hidden layer neurons:

[[*w<sub>10</sub>*, *w<sub>11</sub>*, *w<sub>12</sub>*, ... , *w<sub>1N</sub>* ], </br>
 [*w<sub>20</sub>*, *w<sub>21</sub>*, *w<sub>22</sub>*, ... , *w<sub>2N</sub>* ], </br>
 [*w<sub>30</sub>*, *w<sub>31</sub>*, *w<sub>32</sub>*, ... , *w<sub>3N</sub>* ], </br>
 . </br>
 . </br>
 . </br>
 [*w<sub>H0</sub>*, *w<sub>H1</sub>*, *w<sub>H2</sub>*, ... , *w<sub>HN</sub>* ]]

This is 

## Setup

Suppose you want a network with *N* inputs, *H* hidden nodes, and a single output node (representing a system with 2 classes).

The weights and biases connecting the inputs to the hidden layer nodes can be organized in a *N x H* matrix. Each **row** represents the full set of input weights for one hidden-layer node:

```
[ set of all weights for hidden node 1 ]
[ set of all weights for hidden node 2 ]
[                   .                  ]
[                   .                  ]
[                   .                  ]
[ set of all weights for hidden node H ]
```

If you set things up like this, then the weighted sums at the hidden layer are conceptually a matrix-vector product *Wx*, where *x* is the input point as a column vector.

Note that each row includes a bias value as the "zeroth" weight, which is always paired up with an input of 1.

The output weights are a single vector with *H* elements.

Your implementation is going to be built around the following methods:

`sigmoid(x)`: calculate the sigmoid value of input `x`. Used by both the `predict` and `train` functions.

`predict(hidden_weights, output_weights, point)`: classify the input point using the given input-to-hidden-layer weight matrix and the given hidden-to-output-layer weights.

`train(hidden_weights, output_weights, point, target_label, learning_rate)`: perform a classification step and then a backpropagation update to all weights using the given point and target label.

`epoch(hidden_weights, output_weights, training_set, training_labels)`: perform a complete training epoch on the given set of training points with their associated labels. Basically a loop that wraps around the `train` method.

`evaluate(hidden_weights, output_weights, testing_set, testing_labels)`: predict the class (without performing any training) on the given set of test points and report the fraction that are classified correctly. This is the final function used to evaluate the performance of the training network.

You can add other methods or structures as you see fit.

The initial values of all the weights and biases should be **randomized** to values in [-1, 1].

**You must have a variable that controls the number of hidden-layer nodes and your code must work for any reasonable number of hidden-layer nodes**.

**You only need to support one hidden layer**.

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

R.A. Fisher is the most important statistician in history. He made numerous contributions that helped establish the field of statistics as we know it today, including the concept of statistical significance.

The following dataset is probably the most famous one in machine learning history. It comes originally from a paper Fisher wrote in 1936 and consists of a collection of measurements taken from iris flower specimens.

- Each specimen has four measurements: sepal length, sepal width, petal length, and petal width, all in cm. The sepals are the outer green leaves that come up and surround the petals of the flower.

- The specimens belong to one of three species: *iris setosa*, *iris versicolor*, and  *iris virginica*.

- The goal is to predict the species given the four measurements.

<img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg" width=25% />

*iris setosa*

<img src="https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg" width=25% />

*iris versicolor*

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg" width=25% />

*iris virginica*

### Classifying the Flowers

Your goal in the second part of the project is to use your neural network implementation to learn a model that can classify the iris flowers. The most challenging part: there are *three classes*.

First, get the dataset below into your program. How you do this isn't important: copying it to a file and reading the file is a good strategy.

Next, create a test set by randomly selecting 30 items (20% of the total 150). The remaining 120 items will be the training set. Remember that the test set should only be used for the final evaluation of the model and can't be part of the training process. It's desirable, but not required, to randomize the order of the training examples.

Third, create a network with **three output nodes**, one for each class.

- Each node corresponds to one of the three target classes.

- Each output node has **its own set of weights** connecting it to the hidden layer. The output-layer weights are now a 3 row by *H* column matrix, rather than a single *H* element vector.

- When presented with a point in class 1 (the `Iris-setosa` class), the first output node should be 1 and the other two should be 0. The other two classes are similar: the second node should be 1 for points in the `Iris-versicolor` class and the third should be 1 for points in the `Iris-virginica` class.

Suppose, for example, that the first training example is the first point in the dataset:

```
5.1,3.5,1.4,0.2,Iris-setosa
```

`Iris-setosa` is the first class, so we would like the first output node to have value 1 and the other two to be 0.

The weights of the network are initially random, so the output of the three nodes will probably be random values between 0 and 1. Suppose the network produces the following three output values:

```
output of node 1 = .36
output of node 2 = .79
output of node 3 = .12
```

To pick the assigned class, choose the output node with the highest value: node 2 in this case, which corresponds to *iris versicolor*. This is an incorrect classification.

To adjust the weights, use the target output values of 1, 0, and 0.

```
error at node 1 = 1 - .36     <--- Adjust weights to make this output go to 1 for the iris setosa class
error at node 2 = 0 - .79
error at node 3 = 0 - .12
```

The update rules remain the same. Remember: you already had to figure out how to update a matrix of weights for the hidden layer, so updating the output layer weights for a network with multiple output nodes is not that different.

**You don't need to achieve perfect classification**, but you should be able to demonstrate that your network is learning.

### The Dataset

```
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3.0,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
4.6,3.1,1.5,0.2,Iris-setosa
5.0,3.6,1.4,0.2,Iris-setosa
5.4,3.9,1.7,0.4,Iris-setosa
4.6,3.4,1.4,0.3,Iris-setosa
5.0,3.4,1.5,0.2,Iris-setosa
4.4,2.9,1.4,0.2,Iris-setosa
4.9,3.1,1.5,0.1,Iris-setosa
5.4,3.7,1.5,0.2,Iris-setosa
4.8,3.4,1.6,0.2,Iris-setosa
4.8,3.0,1.4,0.1,Iris-setosa
4.3,3.0,1.1,0.1,Iris-setosa
5.8,4.0,1.2,0.2,Iris-setosa
5.7,4.4,1.5,0.4,Iris-setosa
5.4,3.9,1.3,0.4,Iris-setosa
5.1,3.5,1.4,0.3,Iris-setosa
5.7,3.8,1.7,0.3,Iris-setosa
5.1,3.8,1.5,0.3,Iris-setosa
5.4,3.4,1.7,0.2,Iris-setosa
5.1,3.7,1.5,0.4,Iris-setosa
4.6,3.6,1.0,0.2,Iris-setosa
5.1,3.3,1.7,0.5,Iris-setosa
4.8,3.4,1.9,0.2,Iris-setosa
5.0,3.0,1.6,0.2,Iris-setosa
5.0,3.4,1.6,0.4,Iris-setosa
5.2,3.5,1.5,0.2,Iris-setosa
5.2,3.4,1.4,0.2,Iris-setosa
4.7,3.2,1.6,0.2,Iris-setosa
4.8,3.1,1.6,0.2,Iris-setosa
5.4,3.4,1.5,0.4,Iris-setosa
5.2,4.1,1.5,0.1,Iris-setosa
5.5,4.2,1.4,0.2,Iris-setosa
4.9,3.1,1.5,0.1,Iris-setosa
5.0,3.2,1.2,0.2,Iris-setosa
5.5,3.5,1.3,0.2,Iris-setosa
4.9,3.1,1.5,0.1,Iris-setosa
4.4,3.0,1.3,0.2,Iris-setosa
5.1,3.4,1.5,0.2,Iris-setosa
5.0,3.5,1.3,0.3,Iris-setosa
4.5,2.3,1.3,0.3,Iris-setosa
4.4,3.2,1.3,0.2,Iris-setosa
5.0,3.5,1.6,0.6,Iris-setosa
5.1,3.8,1.9,0.4,Iris-setosa
4.8,3.0,1.4,0.3,Iris-setosa
5.1,3.8,1.6,0.2,Iris-setosa
4.6,3.2,1.4,0.2,Iris-setosa
5.3,3.7,1.5,0.2,Iris-setosa
5.0,3.3,1.4,0.2,Iris-setosa
7.0,3.2,4.7,1.4,Iris-versicolor
6.4,3.2,4.5,1.5,Iris-versicolor
6.9,3.1,4.9,1.5,Iris-versicolor
5.5,2.3,4.0,1.3,Iris-versicolor
6.5,2.8,4.6,1.5,Iris-versicolor
5.7,2.8,4.5,1.3,Iris-versicolor
6.3,3.3,4.7,1.6,Iris-versicolor
4.9,2.4,3.3,1.0,Iris-versicolor
6.6,2.9,4.6,1.3,Iris-versicolor
5.2,2.7,3.9,1.4,Iris-versicolor
5.0,2.0,3.5,1.0,Iris-versicolor
5.9,3.0,4.2,1.5,Iris-versicolor
6.0,2.2,4.0,1.0,Iris-versicolor
6.1,2.9,4.7,1.4,Iris-versicolor
5.6,2.9,3.6,1.3,Iris-versicolor
6.7,3.1,4.4,1.4,Iris-versicolor
5.6,3.0,4.5,1.5,Iris-versicolor
5.8,2.7,4.1,1.0,Iris-versicolor
6.2,2.2,4.5,1.5,Iris-versicolor
5.6,2.5,3.9,1.1,Iris-versicolor
5.9,3.2,4.8,1.8,Iris-versicolor
6.1,2.8,4.0,1.3,Iris-versicolor
6.3,2.5,4.9,1.5,Iris-versicolor
6.1,2.8,4.7,1.2,Iris-versicolor
6.4,2.9,4.3,1.3,Iris-versicolor
6.6,3.0,4.4,1.4,Iris-versicolor
6.8,2.8,4.8,1.4,Iris-versicolor
6.7,3.0,5.0,1.7,Iris-versicolor
6.0,2.9,4.5,1.5,Iris-versicolor
5.7,2.6,3.5,1.0,Iris-versicolor
5.5,2.4,3.8,1.1,Iris-versicolor
5.5,2.4,3.7,1.0,Iris-versicolor
5.8,2.7,3.9,1.2,Iris-versicolor
6.0,2.7,5.1,1.6,Iris-versicolor
5.4,3.0,4.5,1.5,Iris-versicolor
6.0,3.4,4.5,1.6,Iris-versicolor
6.7,3.1,4.7,1.5,Iris-versicolor
6.3,2.3,4.4,1.3,Iris-versicolor
5.6,3.0,4.1,1.3,Iris-versicolor
5.5,2.5,4.0,1.3,Iris-versicolor
5.5,2.6,4.4,1.2,Iris-versicolor
6.1,3.0,4.6,1.4,Iris-versicolor
5.8,2.6,4.0,1.2,Iris-versicolor
5.0,2.3,3.3,1.0,Iris-versicolor
5.6,2.7,4.2,1.3,Iris-versicolor
5.7,3.0,4.2,1.2,Iris-versicolor
5.7,2.9,4.2,1.3,Iris-versicolor
6.2,2.9,4.3,1.3,Iris-versicolor
5.1,2.5,3.0,1.1,Iris-versicolor
5.7,2.8,4.1,1.3,Iris-versicolor
6.3,3.3,6.0,2.5,Iris-virginica
5.8,2.7,5.1,1.9,Iris-virginica
7.1,3.0,5.9,2.1,Iris-virginica
6.3,2.9,5.6,1.8,Iris-virginica
6.5,3.0,5.8,2.2,Iris-virginica
7.6,3.0,6.6,2.1,Iris-virginica
4.9,2.5,4.5,1.7,Iris-virginica
7.3,2.9,6.3,1.8,Iris-virginica
6.7,2.5,5.8,1.8,Iris-virginica
7.2,3.6,6.1,2.5,Iris-virginica
6.5,3.2,5.1,2.0,Iris-virginica
6.4,2.7,5.3,1.9,Iris-virginica
6.8,3.0,5.5,2.1,Iris-virginica
5.7,2.5,5.0,2.0,Iris-virginica
5.8,2.8,5.1,2.4,Iris-virginica
6.4,3.2,5.3,2.3,Iris-virginica
6.5,3.0,5.5,1.8,Iris-virginica
7.7,3.8,6.7,2.2,Iris-virginica
7.7,2.6,6.9,2.3,Iris-virginica
6.0,2.2,5.0,1.5,Iris-virginica
6.9,3.2,5.7,2.3,Iris-virginica
5.6,2.8,4.9,2.0,Iris-virginica
7.7,2.8,6.7,2.0,Iris-virginica
6.3,2.7,4.9,1.8,Iris-virginica
6.7,3.3,5.7,2.1,Iris-virginica
7.2,3.2,6.0,1.8,Iris-virginica
6.2,2.8,4.8,1.8,Iris-virginica
6.1,3.0,4.9,1.8,Iris-virginica
6.4,2.8,5.6,2.1,Iris-virginica
7.2,3.0,5.8,1.6,Iris-virginica
7.4,2.8,6.1,1.9,Iris-virginica
7.9,3.8,6.4,2.0,Iris-virginica
6.4,2.8,5.6,2.2,Iris-virginica
6.3,2.8,5.1,1.5,Iris-virginica
6.1,2.6,5.6,1.4,Iris-virginica
7.7,3.0,6.1,2.3,Iris-virginica
6.3,3.4,5.6,2.4,Iris-virginica
6.4,3.1,5.5,1.8,Iris-virginica
6.0,3.0,4.8,1.8,Iris-virginica
6.9,3.1,5.4,2.1,Iris-virginica
6.7,3.1,5.6,2.4,Iris-virginica
6.9,3.1,5.1,2.3,Iris-virginica
5.8,2.7,5.1,1.9,Iris-virginica
6.8,3.2,5.9,2.3,Iris-virginica
6.7,3.3,5.7,2.5,Iris-virginica
6.7,3.0,5.2,2.3,Iris-virginica
6.3,2.5,5.0,1.9,Iris-virginica
6.5,3.0,5.2,2.0,Iris-virginica
6.2,3.4,5.4,2.3,Iris-virginica
5.9,3.0,5.1,1.8,Iris-virginica
```

## Tips

Start early! Don't wait until the last minute!

Make sure that you are comfortable with all of the details of the backpropgation algorithm. I recommend reviewing this video: 

- https://www.youtube.com/watch?v=Ilg3gGewQ5U

**Develop incrementally** and check everything. ***DO NOT***, under any circumstances, try to write a huge amount of code without testing it.

Start with very small networks and print their outputs and training updates. Verify that the weights are changing the way they should.
