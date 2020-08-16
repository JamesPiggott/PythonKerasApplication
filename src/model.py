import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
import importlib

class Model:

    def __init__(self):
        print("")
        self.model = ""
        self.history = ""


    def define_model(self):
        print("Define the model")
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 3)),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2,2), 
            tf.keras.layers.Conv2D(64, (3,3), activation='relu'), 
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Flatten(), 
            tf.keras.layers.Dense(512, activation='relu'), 
            tf.keras.layers.Dense(1, activation='sigmoid')  
        ])

        self.model.summary()


    def set_optimizer(self):
        print("Setting the optimizer")
        self.model.compile(optimizer=RMSprop(lr=0.001),
              loss='binary_crossentropy',
              metrics = ['accuracy'])


    def set_data_augmentation(self):
        print("Setting data augmentation")

    def load_model(self, model_name):
        """Load a pre-trained for transfer learning. Unless name is specified 'my_model.h5' is used
        

        Parameters:
        model_name (string): Name of pre-trained model that needs to be loaded

        """

    def load_model_from_project(self, project_name):
        print(project_name)
        module_name = project_name
        module = importlib.import_module(module_name,package="Model")
        print(module.__doc__)