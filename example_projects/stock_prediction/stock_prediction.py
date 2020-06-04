import tensorflow as tf
import subprocess
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM,Dense
from sklearn.preprocessing import MinMaxScaler
from subprocess import check_output
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class StockPrediction:

    # Data variables
    data = ""
    train_X = ""
    train_Y = ""
    test_X  = ""
    test_Y  = ""
    scaler = ""

    # Model variables
    model = ""
    history = ""
    epochs = ""

    def __init__(self):
        self.data = ""
        self.train_X = ""
        self.train_Y = ""
        self.test_X = ""
        self.test_Y = ""
        self.scaler = ""
        self.load_data()
        self.convert_data()
        self.define_model(1, 64)
        self.set_optimizer()
        self.train_model()
        self.evaluate_model()
        self.store_model("example_projects/stock_prediction/")

    def load_data(self): 
        data = pd.read_csv('example_projects/stock_prediction/all_stocks_5yr.csv')
        self.data = data[data['Name'] == 'MMM'].close   

    def convert_data(self):
        self.scaler = MinMaxScaler()

        #Scale the data
        self.data = self.data.values.reshape(self.data.shape[0],1)
        self.data = self.scaler.fit_transform(self.data)

        # Reshape the data
        X, Y = self.processData(self.data,7)
        self.train_X, self.test_X = X[:int(X.shape[0]*0.80)],X[int(X.shape[0]*0.80):]
        self.train_Y, self.test_Y = Y[:int(Y.shape[0]*0.80)],Y[int(Y.shape[0]*0.80):]

    def processData(self, data, lb):
            X,Y = [],[]
            for i in range(len(data)-lb-1):
                X.append(data[i:(i+lb),0])
                Y.append(data[(i+lb),0])
            return np.array(X),np.array(Y)

    def define_model(self, epochs, batch_size):

        self.batch_size = batch_size
        self.epochs = epochs

        # The complete model
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.LSTM(256,input_shape=(7,1)),
            tf.keras.layers.Dense(1)
        ])

        self.model.summary()

    def set_optimizer(self):
        self.model.compile(optimizer='adam', loss='mse')


    def train_model(self):
        self.train_X = self.train_X.reshape((self.train_X.shape[0],self.train_X.shape[1],1))
        self.test_X = self.test_X.reshape((self.test_X.shape[0],self.test_X.shape[1],1))

        self.history = self.model.fit(self.train_X, self.train_Y,epochs=10,validation_data=(self.test_X, self.test_Y),shuffle=False)

    def evaluate_model(self):
        print("Evaluating the model")

        # Plot the results
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.show()
        
        # Predict
        Xt = self.model.predict(self.test_X)
        plt.plot(self.scaler.inverse_transform(self.test_Y.reshape(-1,1)))
        plt.plot(self.scaler.inverse_transform(Xt))
        plt.show()

    def store_model(self, path):
        print("Store the model")
        saved_model_path = "/my_model.h5"
        self.model.save(path + saved_model_path)
