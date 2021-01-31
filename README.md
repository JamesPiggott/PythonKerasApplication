# Auto Deep Learning

As the name would suggest Auto Deep Learning allows developers to automatically create Deep Learning models, using the [Keras](https://keras.io/) API. This application provides the project management that is needed besides training. All relevant details are stored on a project file which can be re-used. This project file can be used to set up an automated training pipeline.

To jumpstart your Deep Learning project several showcase examples have been implemented using the Keras API.  Auto Deep Learning is written with Python 3 and adheres to the OOP-paradigm. It has been tested in Windows 10 and Ubuntu 20.10. Tensorflow 2 is used as the back-end Machine Learning framework.

Currently, this project is in early-alpha development and nowhere near feature complete. In time a GUI using Kivy, use of Docker containers and dataset versioning will be implemented. Models trained with Auto Deep Learning can be converted to TensorFlow Lite for mobile use. They can also be deployed for testing on REST server.

## To start Auto Deep Learning

Command to install dependencies

$ pip3 install -r requirements.txt

Command to start the application

$ python app.py

## Showcase projects

The following showcase application are available.

1. Neural Network using Boston Housing data.
2. Convolutional Neural Network using Fashion MNIST.
3. Recurrent Neural Network using stock market data.
4. MNIST Autoencoder.
5. Advanced Convolutional Neural Network for Exoplanet detection.

## Resources
https://github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/save_and_load.ipynb
https://leimao.github.io/blog/Save-Load-Inference-From-TF2-Frozen-Graph/
https://medium.com/free-code-camp/build-a-handwriting-recognizer-ship-it-to-app-store-fcce24205b4b