from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import boston_housing
from keras.models import model_from_json

class KerasStart:

    def start(self, epochs, model_save_choice):

        # Load the data
        (X_train, Y_train), (X_test, Y_test) = boston_housing.load_data()

        # Retrieve the number of variables per input
        nFeatures = X_train.shape[1]

        # Create the Neural Net model
        model = Sequential()
        model.add(Dense(1, input_shape=(nFeatures,), activation='linear'))  # linear, tanh, relu, sigmoid

        # Configure the learning process (optimizer, loss function
        model.compile(optimizer='rmsprop', loss='mse', metrics=['mse', 'mae'])

        # Train the model 1000 times over with the same input - verbose can be {0, 1, 2}
        model.fit(X_train, Y_train, batch_size=4, epochs=epochs, verbose=2)

        # Test the accuracy of the trained model
        scores = model.evaluate(X_test, Y_test)
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]))

        # Display a summary of the model
        model.summary()

        if model_save_choice == True:

            # Saving the model
            # serialize model to JSON and save as .json file
            model_json = model.to_json()
            with open("boston_model.json", "w") as json_file:
                json_file.write(model_json)

            # serialize weights to HDF5 and save as .h5 file
            model.save_weights("boston_model.h5")
            print("Saved model to disk")

        print("We are done!")

    def test_number(self):
        return 10;

if __name__ == "__main__":
    start()
