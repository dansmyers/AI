# Perceptron Training Practice

Let's practice, *just one time*, training a perceptron by hand.

- Yes, this is a bit tedious
- But it's very important that you understand what the model is actually learning
- Having a solid understanding of the single perceptron will help you understand multilayer perceptrons, which are the foundation of deep neural networks

Consider the logical OR function defined over four two-dimensional inputs with target class *t*.

```
x_1   x_2   |   t
-------------------
 0     0    |   0
 0     1    |   1
 1     0    |   1
 1     1    |   1
```

Train a perceptron to correctly classify this data set

- Initialize both input weights and the bias to zero
- Use a learning rate of .1

Everything should converge at the beginning of the *third iteration*.

Once you've finished training, plot the data set (by hand) in two dimensions, then write down the equation of the separating line and add it to your plot. Add the normal vector showing the orientation of the classification boundary.
