from keras.models import Model
from keras import layers
from keras import Input

# Create dummy dataset
import numpy as np
x_train = np.random.random((1000, 64))
y_train = np.random.random((1000, 10))

# Belowan example of the functional API provided by Keras
input_tensor = Input(shape=(64,))
x = layers.Dense(32, activation='relu')(input_tensor)
x = layers.Dense(32, activation='relu')(x)
output_tensor = layers.Dense(10, activation='softmax')(x)

# Instantiating the model
model = Model(input_tensor, output_tensor)

model.summary()

# Compile
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

# Train
model.fit(x_train, y_train, epochs=10, batch_size=128)

# Evaluate
score = model.evaluate(x_train, y_train)