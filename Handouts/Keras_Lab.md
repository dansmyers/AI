Deep Learning with Keras
========================

Setup
-----
Log in to Repl.it. If you have a Python *Data Science* workspace (not just the regular Python workspace) from our previous lab, you can use that. If not, make a new one.

Starting Code
-------------
```
# Multi-layer feed-forward neural networks with Keras

from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop


batch_size = 128
num_classes = 10
epochs = 20

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(8, activation='relu', input_shape=(784,)))
model.add(Dropout(0.1))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```
    
Neural Networks
---------------
Create a new file named `neural_net.py`, copy the starting code to it, and run the example
program.

The early lines load the library and the MNIST handwritten digit data, then convert
the 28 x 28 image data into a vector of 784 elements for input to the
network.

The lines that set up the model are:

```
model = Sequential()
model.add(Dense(8, activation='relu', input_shape=(784,)))
model.add(Dropout(0.1))
model.add(Dense(10, activation='softmax'))
```    

`Sequential()` creates a feed-forward neural network model.

The `Dense` lines create layers of neurons that are densely connected:
every input to the layer  is connected to every neuron in the layer.

The final layer is the output layer, which has 10 classes, one for
each of the 10 handwritten digits. `softmax` is an output
activation function that can be used with more than 2 classes.

`Dropout` is a regularization strategy that improves the network's
performance. During each training iteration, it randomly removes
each neuron with the specified probability. Randomly dropping neurons
forces the other neurons to adapt themselves to compensate, leading
to better overall representations at the hidden layer. Dropout
prevents any one neuron from becoming "too strong" in learned model.

Run the program with the following configurations. For each trial,
note the final accuracy achieved on the test set.
- A hidden layer of 8 neurons
- A hidden layer of 32 neurons
- A hidden layer of 256 neurons
- A hidden layer of 2048 neurons (reduce `num_epochs` to 5)
    
Question: is there a pattern of diminishing returns when adding
larger numbers of neurons to the hidden layer? Why do you think this
might be the case?

Question: compare the performance of the model with 2048 neurons
on its training set vs. its testing set. Do the results indicate
the possibility of the model ** overfitting ** the training data?
    
We Have to Go Deeper
--------------------
Now, experiment with adding additional layers by adding more lines
to the model description. An example two-layer network would look
like the following:

```
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(784,)))
model.add(Dropout(0.1))
model.add(Dense(8, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(10, activation='softmax'))
```

Experiment with some two and three layer architectures. What is the
best result you can obtain?

You don't need to train the network to completion each time, just
monitor the testing accuracy of each epoch.


Convolutional Nets
------------------
Although the feed-forward multi-layer perceptron can do a decent job on this type of problem, there are some
reasons to consider developing a different architecture:

- The input to the model is a 784 element vector. If the first hidden layer has *h* neurons, there are 784*h* parameters just for the input layer.

- More seriously, the input to the network takes the 28x28 image and *flattens* it into a linear 784-element vector. The fact that the input is really a 2D image is lost by the flattening process. The network, in theory, can still learn useful features from the linear input vector, but it would be desirable to use a network that could learn features taken more directly from the 2D input image.

The **concolutional neural network** is an alternate architecture that achieves the second goal. Rather than flattening the image into a linear vector, it uses a series of image processing filters to extract useful features from the 2D input. CNNs have been hugely successful at image processing and classification tasks. We'll talk about the details of the CNN architecture in our next class, but to start, let's see a CNN's performance on the digit classification task compares to a regular MLP.

Create a new file and enter the code below:

```
# Convolutional neural network in Keras

import numpy as np
np.random.seed(123)  # for reproducibility
 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras.optimizers import RMSprop
 
# 4. Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
 
# 5. Preprocess input data
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
 
# 6. Preprocess class labels
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)
 
# 7. Define model architecture
model = Sequential()
 
model.add(Convolution2D(8, (3, 3), activation='relu', input_shape=(28,28, 1)))
model.add(Convolution2D(8, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))
 
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(10, activation='softmax'))
 
# 8. Compile model
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])
 
# 9. Fit model on training data
model.fit(X_train, Y_train, 
          batch_size=32, 
          epochs=10, 
          verbose=1,
          validation_data=(X_test, Y_test))
 
# 10. Evaluate model on test data
score = model.evaluate(X_test, Y_test, verbose=0)
```

The training for this network is quite a bit slower than the basic
feed-forward networks, but it achieves results that are competitive
with the best two and three layer networks after only a single
epoch of training.
