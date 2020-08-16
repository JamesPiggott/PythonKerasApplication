import numpy as np
import tensorflow as tf
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

class Inference:

    def __init__(self):
        print("")

    def perform_tflite_inference(self, path, project_name):
        interpreter = tf.lite.Interpreter(model_path=path + "/" + project_name + "/my_models/" + project_name + ".tflite")
        interpreter.allocate_tensors()

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        print(input_details)
        print(output_details)

        directory = "../Projects/" + project_name + "/sample_images/"
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                print(filename)

                input_image = self.load_image(directory, filename)

                interpreter.set_tensor(input_details[0]['index'], input_image)

                interpreter.invoke()

                output_data = interpreter.get_tensor(output_details[0]['index'])
                print(output_data)

    def load_image(self, path, name):
        img = load_img(path + name, grayscale=False, target_size=(150, 150))
        img = img_to_array(img)
        img = img.reshape(1, 150, 150, 3)
        img = img.astype('float32')
        img = img / 255.0
        return img