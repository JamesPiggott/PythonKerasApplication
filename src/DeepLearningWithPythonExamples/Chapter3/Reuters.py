'''
Created on May 20 2018

@author: James Piggott

Multi-class classification of Reuters articles as described by Francois Chollet in Deep Learning with Python

Reuters newswires and their topics published in 1986
'''

from keras import models
from keras import layers
from keras.datasets import reuters
from keras.utils.np_utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

MAX_VALUE = 10000
MAX_VALIDATE = 1000

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=MAX_VALUE)

def vectorize_sequences(sequences, dimension=MAX_VALUE):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(MAX_VALUE,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

x_val = x_train[:MAX_VALIDATE]
partial_x_train = x_train[MAX_VALIDATE:]

y_val = one_hot_train_labels[:MAX_VALIDATE]
partial_y_train = one_hot_train_labels[MAX_VALIDATE:]

history = model.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results = model.evaluate(x_test,one_hot_test_labels)

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

plt.clf()
acc= history.history['acc']
val_acc = history.history['val_acc']

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()