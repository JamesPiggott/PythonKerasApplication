'''
Created on May 19 2018

@author: James Piggott

Binary classification of IMDB reviews as described by Francois Chollet in Deep Learning with Python

IMDB reviews are labeled positive or negative depending on words used
'''

from keras import models
from keras import layers
from keras.datasets import imdb
import numpy as np
import matplotlib.pyplot as plt

MAX_VALUE = 8000

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=MAX_VALUE)

def vectorize_sequences(sequences, dimension=MAX_VALUE):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(MAX_VALUE,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

x_val = x_train[:MAX_VALUE]
partial_x_train = x_train[MAX_VALUE:]

y_val = y_train[:MAX_VALUE]
partial_y_train = y_train[MAX_VALUE:]

history = model.fit(partial_x_train, partial_y_train, epochs=4, batch_size=512, validation_data=(x_val, y_val))

model.predict(x_test)

## Display the final results in 2 plots
history_dict = history.history
history_dict.keys()

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

# "bo"for "blue dot"
plt.plot(epochs, loss, 'bo', label='Training loss')
# bfor "solid blue line"
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

plt.clf()   # clear figure
acc_values = history_dict['acc']
val_acc_values = history_dict['val_acc']

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()


