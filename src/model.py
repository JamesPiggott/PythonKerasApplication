import tensorflow as tf
import os
from tensorflow.keras.optimizers import RMSprop


class Model:

    def __init__(self, manager):
        self.manager = manager
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

    def load_model_from_text_file(self):
        """Return model with layers of trainign and inference features

        If the text file conforms to the correct Keras syntax then every line will be interpreted as being part
        of a functional model.
        """
        model_file_location = os.path.join(self.manager.project_folder, "model", "model.txt")
        try:
            if os.path.exists(model_file_location):
                file = open(model_file_location, "r")
                api_layers = {}
                for line in file:
                    self.interpret_api_layer(line)

                return "Model file opened", self
            else:
                return "Model file could not be opened", None
        except OSError:
            return 'Error: Opening directory. ' + self.manager.project_folder, None

    def interpret_api_layer(self, line):
        if line is not "":
            print(line)
        # else:
