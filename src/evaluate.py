from .model import Model

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class Evaluate:

    model = Model

    def __init__(self, model):
        print("")
        self.model = model


    def evaluate_model(self):
        print("Evaluating the model")

        #-----------------------------------------------------------
        # Retrieve a list of list results on training and test data
        # sets for each training epoch
        #-----------------------------------------------------------
        acc      = self.model.history.history[     'accuracy' ]
        val_acc  = self.model.history.history[ 'val_accuracy' ]
        loss     = self.model.history.history[    'loss' ]
        val_loss = self.model.history.history['val_loss' ]

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

    def evaluate_model_separate(self, model):
        print("Evaluating the model")

        acc      = model.history.history[     'accuracy' ]
        val_acc  = model.history.history[ 'val_accuracy' ]
        loss     = model.history.history[    'loss' ]
        val_loss = model.history.history['val_loss' ]

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
