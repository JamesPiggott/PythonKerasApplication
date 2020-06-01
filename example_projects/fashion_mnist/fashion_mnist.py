import tensorflow as tf

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# import keras
import numpy as np
# import matplotlib.pyplot as plt

# Load the Fashion-MNIST imgaes using Keras/datasets
from keras.datasets import fashion_mnist
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
# from keras.models import Sequential
# from keras.layers import Dense,Dropout,Flatten
# from keras.layers import Conv2D, MaxPooling2D
# from keras.layers.advanced_activations import LeakyReLU

from tensorflow.keras.optimizers import Adam

class FashionMnist:

    # Data variables
    train_X = ""
    train_Y = ""
    test_X  = ""
    test_Y  = ""
    train_Y_one_hot = "" 
    test_Y_one_hot = ""
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
        self.train_Y_one_hot = ""
        self.test_Y_one_hot = ""
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
        self.define_model(10, 64)
        self.set_optimizer()
        self.train_model()
        self.evaluate_model()
        self.store_model("")


    def load_data(self):
        (self.train_X, self.train_Y), (self.test_X, self.test_Y) = fashion_mnist.load_data()
        self.classes = np.unique(self.train_Y)

    def convert_data(self):
        # Image preprocessing
        self.train_X = self.train_X.reshape(-1, 28, 28, 1)
        self.test_X = self.test_X.reshape(-1, 28, 28, 1)

        # Convert image format from int8 to float32
        self.train_X = self.train_X.astype('float32')
        self.test_X = self.test_X.astype('float32')

        # Normalize pixel values to between 0 and 1
        self.train_X = self.train_X / 255
        self.test_X = self.test_X / 255

        # Convert the class labels to a boolean column
        train_Y_one_hot = to_categorical(self.train_Y)
        test_Y_one_hot = to_categorical(self.test_Y)

        print("Result after conversion: ", train_Y_one_hot[0])

        # Split the training set into two: training and validation: 80 % and 20 % ratio
        self.train_X, self.valid_X, self.train_label, self.valid_label = train_test_split(self.train_X,train_Y_one_hot, test_size=0.2, random_state=13)



    def define_model(self, epochs, batch_size):

        self.batch_size = batch_size
        self.epochs = epochs
        num_classes = self.classes

        # The complete model
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, kernel_size=(3, 3),activation='linear',padding='same',input_shape=(28,28,1)),
            tf.keras.layers.LeakyReLU(alpha=0.1),
            tf.keras.layers.MaxPooling2D((2, 2),padding='same'),
            tf.keras.layers.Dropout(0.25),
            tf.keras.layers.Conv2D(64, (3, 3), activation='linear',padding='same'),
            tf.keras.layers.LeakyReLU(alpha=0.1),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2),padding='same'),
            tf.keras.layers.Dropout(0.25),
            tf.keras.layers.Conv2D(128, (3, 3), activation='linear',padding='same'),
            tf.keras.layers.LeakyReLU(alpha=0.1),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2),padding='same'),
            tf.keras.layers.Dropout(0.4),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='linear'),
            tf.keras.layers.LeakyReLU(alpha=0.1),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(num_classes, activation='softmax')
        ])

        self.model.summary()

    def set_optimizer(self):
        self.model.compile(optimizer=Adam(),
              loss='categorical_crossentropy',
              metrics = ['accuracy'])


    def train_model(self):
        self.history = self.model.fit(self.train_X, self.train_label, batch_size=self.batch_size, epochs=self.epochs, verbose=2,validation_data=(self.valid_X, self.valid_label))

    def evaluate_model(self):
        print("Evaluating the model")

        acc      = self.history.history[     'accuracy' ]
        val_acc  = self.history.history[ 'val_accuracy' ]
        loss     = self.history.history[    'loss' ]
        val_loss = self.history.history['val_loss' ]



        #-----------------------------------------------------------
        # Retrieve a list of list results on training and test data
        # sets for each training epoch
        #-----------------------------------------------------------
        epochs   = range(len(acc)) # Get number of epochs

        #------------------------------------------------
        # Plot training and validation accuracy per epoch
        #------------------------------------------------
        plt.plot  ( epochs,     acc, label='Training')
        plt.plot  ( epochs, val_acc, label='Validation')
        plt.title ('Training and validation accuracy')
        plt.legend()
        plt.figure()

        #------------------------------------------------
        # Plot training and validation loss per epoch
        #------------------------------------------------
        plt.plot  ( epochs,     loss, label='Training')
        plt.plot  ( epochs, val_loss, label='Validation')
        plt.legend()
        plt.title ('Training and validation loss')

        plt.show()

    def store_model(self, path):
        print("Store the model")
        saved_model_path = "/my_model.h5"
        self.model.model.save(path + saved_model_path)