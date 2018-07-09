from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import boston_housing

# Load the data
(X_train, Y_train), (X_test, Y_test) = boston_housing.load_data()

# Retrieve the number of variables per input
nFeatures = X_train.shape[1]

# Create the Neural Net model
model = Sequential()
model.add(Dense(1, input_shape=(nFeatures,), activation='linear'))  # linear, tanh, relu, sigmoid

# Configure the learning process (optimizer, loss function
model.compile(optimizer='rmsprop', loss='mse', metrics=['mse', 'mae'])

# Train the model 1000 times over with the same input
model.fit(X_train, Y_train, batch_size=4, epochs=1000, verbose=0)

# Test the accuracy of the trained model
scores = model.evaluate(X_test, Y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]))

# Display a summary of the model
model.summary()
