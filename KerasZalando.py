'''
Created on April 7 2018

@author: James Piggott

Keras example using the Fashion-MNIST images from Zalando
'''

import keras
import numpy as np
import matplotlib.pyplot as plt

# Load the Fashion-MNIST imgaes using Keras/datasets
from keras.datasets import fashion_mnist
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU


def runcode():
    (train_X, train_Y), (test_X, test_Y) = fashion_mnist.load_data()

    # Check the size of the dimensions - there should 6000 images with size 28 * 28
    print('Training data shape : ', train_X.shape, train_Y.shape)

    # And 1000 test images with size 28 * 28
    print('Testing data shape : ', test_X.shape, test_Y.shape)

    # Find the unique numbers from the train labels
    classes = np.unique(train_Y)
    print('Total number of class labels in dataset:', len(classes))
    print('With class labels: ', classes)

    # Print out an image from the dataset
    plt.figure(figsize=[5,5])

    # Display the first image in training data
    plt.subplot(121)
    plt.imshow(train_X[0,:,:], cmap='gray')
    plt.title("Ground Truth : {}".format(train_Y[0]))

    # Display the first image in testing data
    plt.subplot(122)
    plt.imshow(test_X[0,:,:], cmap='gray')
    plt.title("Ground Truth : {}".format(test_Y[0]))

    # Show or do not show the image
    # plt.show()

    # Image preprocessing
    train_X = train_X.reshape(-1, 28, 28, 1)
    test_X = test_X.reshape(-1, 28, 28, 1)

    # Convert image format from int8 to float32
    train_X = train_X.astype('float32')
    test_X = test_X.astype('float32')

    # Normalize pixel values to between 0 and 1
    train_X = train_X / 255
    test_X = test_X / 255

    # Convert the class labels to a boolean column
    train_Y_one_hot = to_categorical(train_Y)
    test_Y_one_hot = to_categorical(test_Y)

    print("Result after conversion: ", train_Y_one_hot[0])

    # Split the training set into two: training and validation: 80 % and 20 % ratio
    train_X,valid_X,train_label,valid_label = train_test_split(train_X,train_Y_one_hot, test_size=0.2, random_state=13)

    # There will three convolutional layers.
    batch_size = 64
    epochs = 20
    num_classes = 10

    # The complete model
    fashion_model = Sequential()
    fashion_model.add(Conv2D(32, kernel_size=(3, 3),activation='linear',padding='same',input_shape=(28,28,1)))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(MaxPooling2D((2, 2),padding='same'))
    fashion_model.add(Dropout(0.25))
    fashion_model.add(Conv2D(64, (3, 3), activation='linear',padding='same'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
    fashion_model.add(Dropout(0.25))
    fashion_model.add(Conv2D(128, (3, 3), activation='linear',padding='same'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
    fashion_model.add(Dropout(0.4))
    fashion_model.add(Flatten())
    fashion_model.add(Dense(128, activation='linear'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(Dropout(0.3))
    fashion_model.add(Dense(num_classes, activation='softmax'))

    # Define loss type and optimizer (multi-class)
    fashion_model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

    # Print out a model of the training data
    fashion_model.summary()

    # Training the model
    fashion_train_dropout = fashion_model.fit(train_X, train_label, batch_size=batch_size,epochs=epochs,verbose=0,validation_data=(valid_X, valid_label))

    # Save the trained model
    fashion_model.save("fashion_model_dropout.h5py")

    # Evaluation of the model
    test_eval = fashion_model.evaluate(test_X,test_Y_one_hot,verbose=0)
    print("Test loss:", test_eval[0])
    print("Test accuracy:", test_eval[1])

    # Plot the details on model accuracy
    accuracy = fashion_train_dropout.history['acc']
    val_accuracy = fashion_train_dropout.history['val_acc']
    loss = fashion_train_dropout.history['loss']
    val_loss = fashion_train_dropout.history['val_loss']
    epochs = range(len(accuracy))
    plt.plot(epochs, accuracy, 'bo', label='Training accuracy')
    plt.plot(epochs, val_accuracy, 'b', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.figure()
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()

    predicted_classes = fashion_model.predict(test_X)
    predicted_classes = np.argmax(np.round(predicted_classes),axis=1)
    predicted_classes.shape, test_Y.shape

    correct = np.where(predicted_classes==test_Y)[0]
    print("Found %d correct labels" % len(correct))
    for i, correct in enumerate(correct[:9]):
        plt.subplot(3,3,i+1)
        plt.imshow(test_X[correct].reshape(28,28), cmap='gray', interpolation='none')
        plt.title("Predicted {}, Class {}".format(predicted_classes[correct], test_Y[correct]))
        plt.tight_layout()

    incorrect = np.where(predicted_classes!=test_Y)[0]
    print("Found %d incorrect labels" % len(incorrect))
    for i, incorrect in enumerate(incorrect[:9]):
        plt.subplot(3,3,i+1)
        plt.imshow(test_X[incorrect].reshape(28,28), cmap='gray', interpolation='none')
        plt.title("Predicted {}, Class {}".format(predicted_classes[incorrect], test_Y[incorrect]))
        plt.tight_layout()

    from sklearn.metrics import classification_report
    target_names = ["Class {}".format(i) for i in range(num_classes)]
    print(classification_report(test_Y, predicted_classes, target_names=target_names))


if __name__ == "__main__":
    runcode()