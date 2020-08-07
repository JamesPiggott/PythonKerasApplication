import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import boston_housing
from keras.models import model_from_json

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class BostonHousing:

    # Data variables
    train_X = ""
    train_Y = ""
    test_X  = ""
    test_Y  = ""
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
        self.classes = ""
        self.model = ""
        self.history = ""
        self.epochs = ""
        self.batch_size = ""

        self.load_data()
        self.define_model(10, 64)
        self.set_optimizer()
        self.train_model()
        self.evaluate_model()
        self.store_model("example_projects/boston_housing/")


    def load_data(self):
        (self.train_X, self.train_Y), (self.test_X, self.test_Y) = boston_housing.load_data()
        self.classes = self.train_X.shape[1]


    def define_model(self, epochs, batch_size):

        self.batch_size = batch_size
        self.epochs = epochs

        # The complete model
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(1, input_shape=(self.classes,), activation='linear')
        ])

        self.model.summary()

    def set_optimizer(self):
        self.model.compile(optimizer='rmsprop', 
                loss='mse', 
                metrics=['mse', 'mae'])


    def train_model(self):
        self.history = self.model.fit(self.train_X, self.train_Y, batch_size=self.batch_size, epochs=self.epochs, verbose=2)


    def evaluate_model(self):
        print("Evaluating the model")

        mse      = self.history.history[     'mse' ]
        mae  = self.history.history[ 'mae' ]

        #------------------------------------------------
        # Plot mse and mae 
        #------------------------------------------------
        plt.plot  ( mse, label='MSE')
        plt.plot  ( mae, label='MAE')
        plt.title ('MSE and MAE accuracy')
        plt.legend()
        plt.show()

    def store_model(self, path):
        print("Store the model")

        # Create 
        self.model.save("my_model")
        # saved_model_path = "/my_model.h5"
        # self.model.save(path + saved_model_path)
