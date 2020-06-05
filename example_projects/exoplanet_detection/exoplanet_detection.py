import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.layers import Convolution1D
from keras.layers import MaxPooling1D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers.normalization import BatchNormalization

class ExoplanetDetection:

    # Data variables
    train_X = ""
    train_Y = ""
    test_X  = ""
    test_Y  = ""

    valid_X = ""
    train_label = ""
    valid_label = ""
    classes = ""

    # Model variables
    model = ""
    history = ""
    epochs = ""
    batch_size = ""

    def __init__(self):
        self.train_X = ""
        self.train_Y = ""
        self.test_X = ""
        self.test_Y = ""

        self.valid_X = ""
        self.train_label = ""
        self.valid_label = ""
        self.classes = ""
        self.model = ""
        self.history = ""
        self.epochs = ""
        self.batch_size = ""

        self.load_data()
        self.convert_data()
        self.define_model(1, 64)
        self.set_optimizer()
        self.train_model()
        self.evaluate_model()
        self.store_model("example_projects/exoplanet_detection/")


    def load_data(self):

        # Importing training set
        training_set = pd.read_csv("example_projects/exoplanet_detection/data/exoTrain.csv")
        self.train_X = training_set.iloc[:,1:].values
        self.train_Y = training_set.iloc[:,0:1].values

        # Importing test set
        test_set = pd.read_csv("example_projects/exoplanet_detection/data/exoTest.csv")
        self.test_X = test_set.iloc[:,1:].values
        self.test_Y = test_set.iloc[:,0:1].values

    def convert_data(self):
        # Scale the data
        sc = StandardScaler()
        self.train_X = sc.fit_transform(self.train_X)
        self.test_X = sc.fit_transform(self.test_X)

        # Convert data into 3d tensor
        self.train_X = np.reshape(self.train_X,(self.train_X.shape[0],self.train_X.shape[1],1))
        self.test_X = np.reshape(self.test_X,(self.test_X.shape[0],self.test_X.shape[1],1))


    def define_model(self, epochs, batch_size):

        self.batch_size = batch_size
        self.epochs = epochs
        # num_classes = self.classes

        # The complete model
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Convolution1D(filters=8, kernel_size=11, activation="relu", input_shape=(3197,1)),
            tf.keras.layers.MaxPooling1D(strides=4),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dropout(0.25),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid'),
        ])

        self.model.summary()

    def set_optimizer(self):
        self.model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])


    def train_model(self):
        self.history = self.model.fit(self.train_X, self.train_Y, batch_size=64, epochs=30, validation_data=(self.test_X,self.test_Y), verbose=2)


    def evaluate_model(self):
        print("Evaluating the model")
        score = self.model.evaluate(self.test_X, self.test_Y)
        print("\n%s: %.2f%%" % (self.model.metrics_names[1], score[1]))


    def store_model(self, path):
        print("Store the model")
        saved_model_path = "/my_model.h5"
        self.model.save(path + saved_model_path)
