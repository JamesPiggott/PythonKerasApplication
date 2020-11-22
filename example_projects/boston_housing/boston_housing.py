import matplotlib.pyplot as plt
import tensorflow as tf
import os
from keras.datasets import boston_housing


class BostonHousing:

    def __init__(self, name):
        model_folder = os.path.join("example_projects", name, "models")

        # self.load_data()
        # self.define_model(100, 64)
        # self.set_optimizer()
        # self.train_model()
        # self.evaluate_model()
        # self.store_model(model_folder)
        self.load_model(model_folder)


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

        # Save model as TensorFlow saved model
        self.model.save(path)

    def load_model(self, path):
        print("Load the model")
        model = tf.keras.models.load_model(path)
        model.summary()
        print(model.layers)
