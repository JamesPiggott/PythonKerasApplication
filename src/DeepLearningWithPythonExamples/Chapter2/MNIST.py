'''
Created on May 16 2018

@author: James Piggott

MNIST handwriting model as described by Francois Chollet in Deep Learning with Python

A.K.A. the 'Hello, world!' of Deep Learning
'''

from keras import models
from keras import layers
from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape the images (matrices) as vectors and normalize
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# Describe the model to be used
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

# Define the optimizer, loss function and metric to evaluate
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Ensure the labels are interpreted as categorical data (0 to 9)
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Train the model
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# Test the model using the test data set
test_loss, test_acc = network.evaluate(test_images, test_labels)

print('test_acc:', test_acc)