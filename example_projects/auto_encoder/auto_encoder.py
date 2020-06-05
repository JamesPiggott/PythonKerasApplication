import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np


class AutoEncoder:

    # Data variables
    train_X = ""
    test_X = ""
    encoding_dim = ""

    # Model variables
    autoencoder = ""
    encoder = ""
    decoder = ""
    epochs = ""

    def __init__(self):
        self.data = ""
        self.train_X = ""
        self.test_X = ""
        self.encoding_dim = ""
        self.autoencoder = ""
        self.encoder = ""
        self.decoder = ""

        self.load_data()
        self.convert_data()
        self.define_model(50, 256, 32)
        self.set_optimizer()
        self.train_model()
        self.evaluate_model()
        self.store_model("example_projects/auto_encoder/")

    def load_data(self): 
        (self.train_X, _), (self.test_X, _) = mnist.load_data()

        self.train_X = self.train_X.astype('float32') / 255.
        self.test_X = self.test_X.astype('float32') / 255. 

    def convert_data(self):
        self.train_X = self.train_X.reshape((len(self.train_X), np.prod(self.train_X.shape[1:])))
        self.test_X = self.test_X.reshape((len(self.test_X), np.prod(self.test_X.shape[1:])))

    def define_model(self, epochs, batch_size, encoding_dim):

        self.batch_size = batch_size
        self.epochs = epochs
        self.encoding_dim = encoding_dim
       
        input_img = Input(shape=(784,))

        encoded = Dense(encoding_dim, activation='relu')(input_img)

        decoded = Dense(784, activation='sigmoid')(encoded)

        self.autoencoder = Model(input_img, decoded)

        self.encoder = Model(input_img, encoded)
        encoded_input = Input(shape=(encoding_dim,))

        decoder_layer = self.autoencoder.layers[-1]
        self.decoder = Model(encoded_input, decoder_layer(encoded_input))

        self.autoencoder.summary()

    def set_optimizer(self):
        self.autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

    def train_model(self):
        self.autoencoder.fit(self.train_X, self.train_X, epochs=50, batch_size=256, shuffle=True, validation_data=(self.test_X, self.test_X))

    def evaluate_model(self):
        print("Evaluating the model")

        # encode and decode some digits
        encoded_imgs = self.encoder.predict(self.test_X)
        decoded_imgs = self.decoder.predict(encoded_imgs)
     
        n = 10  # how many digits we will display
        plt.figure(figsize=(20, 4))
        for i in range(n):

            # display original
            ax = plt.subplot(2, n, i + 1)
            plt.imshow(self.test_X[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

            # display reconstruction
            ax = plt.subplot(2, n, i + 1 + n)
            plt.imshow(decoded_imgs[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

        plt.show()

    def store_model(self, path):
        print("Store the model")
        saved_model_path = "/my_model.h5"
        self.autoencoder.save_weights(path + saved_model_path)

