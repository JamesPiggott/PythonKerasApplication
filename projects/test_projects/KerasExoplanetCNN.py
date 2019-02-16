import pandas as pd
import numpy as np

class KerasExoplanetCNN:

    def start(self, epochs, model_save_choice):

        # Importing training set
        training_set = pd.read_csv("input/exoTrain.csv")
        X_train = training_set.iloc[:,1:].values
        y_train = training_set.iloc[:,0:1].values

        # Importing test set
        test_set = pd.read_csv("input/exoTest.csv")
        X_test = test_set.iloc[:,1:].values
        y_test = test_set.iloc[:,0:1].values

        # Scale the data
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.fit_transform(X_test)

        # Convert data into 3d tensor
        X_train = np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))
        X_test = np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

        # Importing convolutional layers
        from keras.models import Sequential
        from keras.layers import Convolution1D
        from keras.layers import MaxPooling1D
        from keras.layers import Flatten
        from keras.layers import Dense
        from keras.layers import Dropout
        from keras.layers.normalization import BatchNormalization

        # Initialising the CNN
        classifier = Sequential()

        # Input shape must be explicitly defined, DO NOT USE (None,shape)!!!
        # 1.Multiple convolution and max pooling
        classifier.add(Convolution1D(filters=8, kernel_size=11, activation="relu", input_shape=(3197,1)))
        classifier.add(MaxPooling1D(strides=4))
        classifier.add(BatchNormalization())

        # 2.Flattening
        classifier.add(Flatten())

        # 3.Full Connection
        classifier.add(Dropout(0.5))
        classifier.add(Dense(64, activation='relu'))
        classifier.add(Dropout(0.25))
        classifier.add(Dense(64, activation='relu'))
        classifier.add(Dense(1, activation='sigmoid'))

        # Configure the learning process
        classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

        # Train!
        classifier.fit(X_train, y_train, batch_size=64, epochs=epochs, validation_data=(X_test,y_test), verbose=2)

        # Evaluate the model
        score = classifier.evaluate(X_test, y_test)
        print("\n%s: %.2f%%" % (classifier.metrics_names[1], score[1]))

        if model_save_choice == True:

            # Saving the model
            # serialize model to JSON and save as .json file
            model_json = classifier.to_json()
            with open("exoplanet_model.json", "w") as json_file:
                json_file.write(model_json)

            # serialize weights to HDF5 and save as .h5 file
            classifier.save_weights("exoplanet_model.h5")
            print("Saved model to disk")

        print("We are done!")

if __name__ == "__main__":
    start()
