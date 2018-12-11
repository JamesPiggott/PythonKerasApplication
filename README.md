# PythonKerasApplication

### Created April 16 2018
This application is meant to showcase useful examples of applied Deep Learning with the Keras interface. In time it can also be used on new situations. 

Initially it can be used on Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN)

Start the application

python MainApplication.py

Command to install dependencies
$ pip install numpy scipy scikit-learn tensorflow pillow h5py keras

### Python Keras Application Requirements
Below are the basic requirements for this application. They are part of a larger design document ommitted for brevity..
#### High-level design

1.	Project setup
1.1.	The user should be prompted to open an existing project or start a new one. 
1.1.1.	Projects are stored in the projects folder at the highest level within the application.
1.2.	The user should be prompted for a source for the data. 
1.2.1.	This can be either from an online source or copy-pasted by the user.
1.2.2.	In the case the user copy-pastes the data files the system should check if the data folder is not empty before proceeding.
2.	Load the dataset
2.1.	The system should be able to auto-detect the nature of the data: CSV file(s) or other separation methods, images (JPEG and PNG)
2.2.	The user should be prompted for the nature of the project. Is it a Convolutional Neural Network or a Recurrent Neural Network?
2.3.	User choices should be saved in a project meta file. 
2.3.1.	Should the user wish to continue at a later time then their progress will be saved.
3.	Analyze the dataset
4.	Define the model
5.	Train the model
6.	Evaluate trained model
7.	Deploy trained model
8.	Test projects
8.1.	The application should have several well documented test projects users can examine to quickly get under way. These should include.
8.1.1.	 Neural Network using the Boston Housing Data.
8.1.2.	 MNIST-fashion: with data from Zalando a basic CNN is created. This is considered an ‘Hello, world!’ example.
8.1.3.	 Stock market data: used to create a simple Recurrent Neural network.
8.1.4.	 Rest API: a simple coding example using ImageNet whose results can be accessed by REST API commands provided through the Python Flask library.


#### Example projects
In addition to the basic Keras app there are a number of showcase applications. These integrate Keras into everyday applications such as image recognition, a game and stock market app.

1. Simple REST API app: allow user to train and test an image.
2. Simple RNN stock market app.
3. Simple game AI.
4. Simple graph and interface app.
