# Imports
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

import numpy as np

import wandb
from wandb.keras import WandbCallback

# Download dataset
print('[INFO] Downloading MNIST dataset')
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train/255.0
x_test = x_test/255.0

print("X_train: ", x_train.shape)
print("y_train: ", y_train.shape)
print("X_test: ", x_test.shape)
print("y_test: ", y_test.shape)

# Build model

def build_model():
    inputs = Input(shape=(28,28,1))
    x = Conv2D(16, kernel_size=(3,3), activation='relu')(inputs)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Conv2D(32, kernel_size=(3,3), activation='relu')(inputs)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.2)(x)
    outputs = Dense(10, activation='softmax')(x)

    return Model(inputs, outputs)

earlystopper = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                patience=2,
                                                verbose=0,
                                                mode='auto',
                                                restore_best_weights=False)


model = build_model()
model.compile('adam', 'sparse_categorical_crossentropy', ['acc'])

wandb.init(project='test-gpu')

# train
model.fit(x_train,
          y_train,
          epochs=10,
          batch_size=32,
          validation_data=(x_test, y_test),
          callbacks=[WandbCallback(),
                     earlystopper])

# evaluate
model.evaluate(x_test, y_test)