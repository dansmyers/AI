# Perceptron Training

Use the perceptron learning algorithm to learn a separating line for the OR function:
```
 x_1 |  x_2 |  t
------------------
  0  |   0  |  0
  0  |   1  |  1
  1  |   0  |  1
  1  |   1  |  1
```

Let all of the starting weights be 0 and let the learning rate be .1.

Once you've trained the perceptron, draw a 2-d plot showing the four training points and the separating line represented by your weights.

_Without doing any training iterations_, explain how you could adapt your existing weights to classify the NOR function, which is the logical inversion of OR.
```
 x_1 |  x_2 |  t
------------------
  0  |   0  |  1
  0  |   1  |  0
  1  |   0  |  0
  1  |   1  |  0
```
